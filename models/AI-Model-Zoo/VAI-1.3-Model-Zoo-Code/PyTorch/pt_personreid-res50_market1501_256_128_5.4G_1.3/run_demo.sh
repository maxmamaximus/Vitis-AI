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

checkpoint_dir=/group/modelzoo/internal-cooperation-models/pytorch/personreid
#checkpoint_dir=path_to_personreid_model
backbone=resnet50 # resnet50

cd ./code 
python inference.py --model_path ${checkpoint_dir}/personreid_${backbone}.pth --config_file ./configs/personreid_${backbone}.yml 
