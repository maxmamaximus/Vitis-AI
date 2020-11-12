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


export CUDA_VISIBLE_DEVICES=0
export PYTHONPATH=${PWD}/code/test:${PYTHONPATH}

CONFIG=float/config.proto
WEIGHTS=float/float.tckpt
QUANT_DIR=quantized
RESULT=data/preds

export W_QUANT=1
echo "Calibrating model quantization..."
QUANT_MODE=calib
python code/test/test.py -config ${CONFIG} -weights ${WEIGHTS} -pred_dir ${RESULT} -quant_mode ${QUANT_MODE} -quant_dir ${QUANT_DIR}

echo "Testing quantized model..."
QUANT_MODE=test
python code/test/test.py -config ${CONFIG} -weights ${WEIGHTS} -pred_dir ${RESULT} -quant_mode ${QUANT_MODE} -quant_dir ${QUANT_DIR}

echo "Dumping xmodel..."
QUANT_MODE=test
python code/test/test.py -config ${CONFIG} -weights ${WEIGHTS} -pred_dir ${RESULT} -quant_mode ${QUANT_MODE} -quant_dir ${QUANT_DIR} -dump_xmodel
