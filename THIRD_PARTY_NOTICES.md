# Third-party notices

## TorchVision source excerpts

The object detection and segmentation notebook uses `inspect.getsource()` to explain TorchVision internals. Its saved outputs contain excerpts from TorchVision, including detection heads, region proposals, pooling, and loss functions. These excerpts retain TorchVision's BSD 3-Clause license.

Source: [pytorch/vision](https://github.com/pytorch/vision). [Upstream license](https://github.com/pytorch/vision/blob/main/LICENSE):

```text
BSD 3-Clause License

Copyright (c) Soumith Chintala 2016,
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

## Models and datasets

Model weights, adapters, and downloaded datasets are not included in this repository. Their licenses and access terms are provided by their respective publishers:

- [TorchVision pretrained models](https://docs.pytorch.org/vision/stable/models.html)
- [DETR ResNet-50](https://huggingface.co/facebook/detr-resnet-50)
- [Stable Diffusion XL](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)
- [Watercolor SDXL LoRA](https://huggingface.co/ostris/watercolor_style_lora_sdxl)
- [MedGemma 1.5 4B](https://huggingface.co/google/medgemma-1.5-4b-it)
- [Brain MRI Images for Brain Tumor Detection](https://www.kaggle.com/datasets/navoneel/brain-mri-images-for-brain-tumor-detection)

The MedGemma notebook retains an example MRI visualization from the linked dataset in its saved outputs. The course's Apache 2.0 license does not replace the terms of this third-party content.

The oranges and cabin input images were generated with ChatGPT and provided by the course author. Their provenance is stated beside the image-loading examples in the notebooks.
