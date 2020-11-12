# Copyright 2019 Xilinx Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

export PYTHONPATH=${PWD}:${PYTHONPATH}
CUDA_VISIBLE_DEVICES=0 python code/test.py \
  --input_size 128,128 \
  --img_path ./data/nuclei_data/ \
  --weight_file ./quantized/quantized.h5 \
  --quantize true \
  --num_classes 2 \
  --save_path results_visulization 
