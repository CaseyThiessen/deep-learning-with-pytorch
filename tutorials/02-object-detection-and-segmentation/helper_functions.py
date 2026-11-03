from __future__ import annotations

import inspect
import textwrap
from pathlib import Path
from typing import Dict, List, Mapping, Sequence

import torch
import torchvision
from torchvision.ops import box_iou, nms
from torchvision.utils import draw_bounding_boxes, draw_segmentation_masks
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from IPython.display import Markdown, display



def show_image_tensor(image_tensor: torch.Tensor, title: str | None = None, figsize=(10, 8)):
    """Display a CHW tensor in [0, 1] or [0, 255]."""
    image = image_tensor.detach().cpu()
    if image.dtype != torch.uint8:
        image = (image.clamp(0, 1) * 255).to(torch.uint8)
    image = image.permute(1, 2, 0)

    plt.figure(figsize=figsize)
    plt.imshow(image)
    plt.axis("off")
    if title:
        plt.title(title)
    plt.show()


def pil_to_tensor_uint8(image: Image.Image) -> torch.Tensor:
    """Convert a PIL image to a uint8 tensor with shape [C, H, W]."""
    return torch.as_tensor(
        list(image.convert("RGB").getdata()), dtype=torch.uint8
    ).reshape(image.height, image.width, 3).permute(2, 0, 1)


def pil_to_tensor_float(image: Image.Image) -> torch.Tensor:
    """Convert a PIL image to a float tensor in [0, 1] with shape [C, H, W]."""
    return pil_to_tensor_uint8(image).float() / 255.0


def show_source(obj, title: str | None = None, max_lines: int | None = 120):
    """
    Display Python source code for a class, function, method, or module method.

    Long functions are deliberately truncated so the notebook stays readable.
    """
    try:
        source = inspect.getsource(obj)
    except (OSError, TypeError) as error:
        print(f"Could not retrieve source for {obj}: {error}")
        print("This often happens for compiled, C++/CUDA-backed, or dynamically generated functions.")
        return

    source = textwrap.dedent(source)
    lines = source.splitlines()

    if max_lines is not None and len(lines) > max_lines:
        omitted = len(lines) - max_lines
        lines = lines[:max_lines]
        lines.append(f"# ... {omitted} more lines omitted to keep the notebook readable ...")
        source = "\n".join(lines)

    if title:
        display(Markdown(f"### {title}"))

    display(Markdown(f"```python\n{source}\n```"))


def category_name(categories: Sequence[str] | Mapping[int, str], label: torch.Tensor | int) -> str:
    """Convert a model class index into a readable class name."""
    idx = int(label)
    if isinstance(categories, Mapping):
        return str(categories.get(idx, idx))
    if 0 <= idx < len(categories):
        return str(categories[idx])
    return str(idx)


def visualize_detection_prediction(
    image_uint8: torch.Tensor,
    prediction: Dict[str, torch.Tensor],
    categories: Sequence[str] | Mapping[int, str],
    score_threshold: float = 0.6,
    max_detections: int = 10,
    title: str = "Predictions",
):
    """Draw high-confidence detection boxes on an image tensor."""
    pred = {k: v.detach().cpu() for k, v in prediction.items()}

    keep = pred["scores"] >= score_threshold
    boxes = pred["boxes"][keep][:max_detections]
    labels = pred["labels"][keep][:max_detections]
    scores = pred["scores"][keep][:max_detections]

    if boxes.numel() == 0:
        show_image_tensor(image_uint8, title=f"{title}: no predictions above threshold")
        return

    label_text = [
        f"{category_name(categories, label)}: {float(score):.2f}"
        for label, score in zip(labels, scores)
    ]

    drawn = draw_bounding_boxes(
        image_uint8,
        boxes=boxes.to(torch.int64),
        labels=label_text,
        width=3,
    )
    show_image_tensor(drawn, title=title)


def visualize_instance_segmentation_prediction(
    image_uint8: torch.Tensor,
    prediction: Dict[str, torch.Tensor],
    categories: Sequence[str] | Mapping[int, str],
    score_threshold: float = 0.7,
    mask_threshold: float = 0.5,
    max_instances: int = 5,
    title: str = "Mask R-CNN predictions",
):
    """Draw high-confidence instance masks and boxes on an image tensor."""
    pred = {k: v.detach().cpu() for k, v in prediction.items()}
    keep = pred["scores"] >= score_threshold

    boxes = pred["boxes"][keep][:max_instances]
    labels = pred["labels"][keep][:max_instances]
    scores = pred["scores"][keep][:max_instances]

    if boxes.numel() == 0:
        show_image_tensor(image_uint8, title=f"{title}: no predictions above threshold")
        return

    # TorchVision prediction["masks"] contains mask probabilities. Threshold them
    # into binary foreground masks for visualization.
    masks = pred["masks"][keep][:max_instances, 0] >= mask_threshold

    label_text = [
        f"{category_name(categories, label)}: {float(score):.2f}"
        for label, score in zip(labels, scores)
    ]

    image_with_masks = draw_segmentation_masks(
        image_uint8,
        masks=masks,
        alpha=0.5,
    )

    image_with_boxes = draw_bounding_boxes(
        image_with_masks,
        boxes=boxes.to(torch.int64),
        labels=label_text,
        width=3,
    )

    show_image_tensor(image_with_boxes, title=title)
