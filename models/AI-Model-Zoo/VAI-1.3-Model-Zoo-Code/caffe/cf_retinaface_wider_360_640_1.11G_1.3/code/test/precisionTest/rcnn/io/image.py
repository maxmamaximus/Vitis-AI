# Apache License
# 
# Version 2.0, January 2004
# 
# http://www.apache.org/licenses/
# 
# TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
# 
# 1. Definitions.
# 
# "License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document.
# 
# "Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License.
# 
# "Legal Entity" shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common control with that entity. For the purposes of this definition, "control" means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the outstanding shares, or (iii) beneficial ownership of such entity.
# 
# "You" (or "Your") shall mean an individual or Legal Entity exercising permissions granted by this License.
# 
# "Source" form shall mean the preferred form for making modifications, including but not limited to software source code, documentation source, and configuration files.
# 
# "Object" form shall mean any form resulting from mechanical transformation or translation of a Source form, including but not limited to compiled object code, generated documentation, and conversions to other media types.
# 
# "Work" shall mean the work of authorship, whether in Source or Object form, made available under the License, as indicated by a copyright notice that is included in or attached to the work (an example is provided in the Appendix below).
# 
# "Derivative Works" shall mean any work, whether in Source or Object form, that is based on (or derived from) the Work and for which the editorial revisions, annotations, elaborations, or other modifications represent, as a whole, an original work of authorship. For the purposes of this License, Derivative Works shall not include works that remain separable from, or merely link (or bind by name) to the interfaces of, the Work and Derivative Works thereof.
# 
# "Contribution" shall mean any work of authorship, including the original version of the Work and any modifications or additions to that Work or Derivative Works thereof, that is intentionally submitted to Licensor for inclusion in the Work by the copyright owner or by an individual or Legal Entity authorized to submit on behalf of the copyright owner. For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication sent to the Licensor or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, the Licensor for the purpose of discussing and improving the Work, but excluding communication that is conspicuously marked or otherwise designated in writing by the copyright owner as "Not a Contribution."
# 
# "Contributor" shall mean Licensor and any individual or Legal Entity on behalf of whom a Contribution has been received by Licensor and subsequently incorporated within the Work.
# 
# 2. Grant of Copyright License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.
# 
# 3. Grant of Patent License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by such Contributor that are necessarily infringed by their Contribution(s) alone or by combination of their Contribution(s) with the Work to which such Contribution(s) was submitted. If You institute patent litigation against any entity (including a cross-claim or counterclaim in a lawsuit) alleging that the Work or a Contribution incorporated within the Work constitutes direct or contributory patent infringement, then any patent licenses granted to You under this License for that Work shall terminate as of the date such litigation is filed.
# 
# 4. Redistribution. You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions:
# 
# You must give any other recipients of the Work or Derivative Works a copy of this License; and
# You must cause any modified files to carry prominent notices stating that You changed the files; and
# You must retain, in the Source form of any Derivative Works that You distribute, all copyright, patent, trademark, and attribution notices from the Source form of the Work, excluding those notices that do not pertain to any part of the Derivative Works; and
# If the Work includes a "NOTICE" text file as part of its distribution, then any Derivative Works that You distribute must include a readable copy of the attribution notices contained within such NOTICE file, excluding those notices that do not pertain to any part of the Derivative Works, in at least one of the following places: within a NOTICE text file distributed as part of the Derivative Works; within the Source form or documentation, if provided along with the Derivative Works; or, within a display generated by the Derivative Works, if and wherever such third-party notices normally appear. The contents of the NOTICE file are for informational purposes only and do not modify the License. You may add Your own attribution notices within Derivative Works that You distribute, alongside or as an addendum to the NOTICE text from the Work, provided that such additional attribution notices cannot be construed as modifying the License.
# 
# You may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such Derivative Works as a whole, provided Your use, reproduction, and distribution of the Work otherwise complies with the conditions stated in this License.
# 5. Submission of Contributions. Unless You explicitly state otherwise, any Contribution intentionally submitted for inclusion in the Work by You to the Licensor shall be under the terms and conditions of this License, without any additional terms or conditions. Notwithstanding the above, nothing herein shall supersede or modify the terms of any separate license agreement you may have executed with Licensor regarding such Contributions.
# 
# 6. Trademarks. This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor, except as required for reasonable and customary use in describing the origin of the Work and reproducing the content of the NOTICE file.
# 
# 7. Disclaimer of Warranty. Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.
# 
# 8. Limitation of Liability. In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall any Contributor be liable to You for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising as a result of this License or out of the use or inability to use the Work (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if such Contributor has been advised of the possibility of such damages.
# 
# 9. Accepting Warranty or Additional Liability. While redistributing the Work or Derivative Works thereof, You may choose to offer, and charge a fee for, acceptance of support, warranty, indemnity, or other liability obligations and/or rights consistent with this License. However, in accepting such obligations, You may act only on Your own behalf and on Your sole responsibility, not on behalf of any other Contributor, and only if You agree to indemnify, defend, and hold each Contributor harmless for any liability incurred by, or claims asserted against, such Contributor by reason of your accepting any such warranty or additional liability.
# 
# END OF TERMS AND CONDITIONS

from __future__ import print_function
import numpy as np
import cv2
import os
import math
import sys
import random
from ..config import config

def brightness_aug(src, x):
  alpha = 1.0 + random.uniform(-x, x)
  src *= alpha
  return src

def contrast_aug(src, x):
  alpha = 1.0 + random.uniform(-x, x)
  coef = np.array([[[0.299, 0.587, 0.114]]])
  gray = src * coef
  gray = (3.0 * (1.0 - alpha) / gray.size) * np.sum(gray)
  src *= alpha
  src += gray
  return src

def saturation_aug(src, x):
  alpha = 1.0 + random.uniform(-x, x)
  coef = np.array([[[0.299, 0.587, 0.114]]])
  gray = src * coef
  gray = np.sum(gray, axis=2, keepdims=True)
  gray *= (1.0 - alpha)
  src *= alpha
  src += gray
  return src

def color_aug(img, x):
  if config.COLOR_MODE>1:
    augs = [brightness_aug, contrast_aug, saturation_aug]
    random.shuffle(augs)
  else:
    augs = [brightness_aug]
  for aug in augs:
    #print(img.shape)
    img = aug(img, x)
    #print(img.shape)
  return img

def get_image(roidb, scale=False):
    """
    preprocess image and return processed roidb
    :param roidb: a list of roidb
    :return: list of img as in mxnet format
    roidb add new item['im_info']
    0 --- x (width, second dim of im)
    |
    y (height, first dim of im)
    """
    num_images = len(roidb)
    processed_ims = []
    processed_roidb = []
    for i in range(num_images):
        roi_rec = roidb[i]
        if 'stream' in roi_rec:
          im = cv2.imdecode(roi_rec['stream'], cv2.IMREAD_COLOR)
        else:
          assert os.path.exists(roi_rec['image']), '{} does not exist'.format(roi_rec['image'])
          im = cv2.imread(roi_rec['image'])
        if roidb[i]['flipped']:
            im = im[:, ::-1, :]
        new_rec = roi_rec.copy()
        if scale:
          scale_range = config.TRAIN.SCALE_RANGE
          im_scale = np.random.uniform(scale_range[0], scale_range[1])
          im = cv2.resize(im, None, None, fx=im_scale, fy=im_scale, interpolation=cv2.INTER_LINEAR)
        elif not config.ORIGIN_SCALE:
          scale_ind = random.randrange(len(config.SCALES))
          target_size = config.SCALES[scale_ind][0]
          max_size = config.SCALES[scale_ind][1]
          im, im_scale = resize(im, target_size, max_size, stride=config.IMAGE_STRIDE)
        else:
          im_scale = 1.0
        im_tensor = transform(im, config.PIXEL_MEANS, config.PIXEL_STDS,im_scale)
        if 'boxes_mask' in roi_rec:
          im = im.astype(np.float32)
          boxes_mask = roi_rec['boxes_mask'].copy() * im_scale
          boxes_mask = boxes_mask.astype(np.int)
          for j in xrange(boxes_mask.shape[0]):
            m = boxes_mask[j]
            im_tensor[:,:,m[1]:m[3],m[0]:m[2]] = 0.0
            #print('find mask', m, file=sys.stderr)
        processed_ims.append(im_tensor)
        new_rec['boxes'] = roi_rec['boxes'].copy() * im_scale
        if config.TRAIN.IMAGE_ALIGN>0:
          if im_tensor.shape[2]%config.TRAIN.IMAGE_ALIGN!=0 or im_tensor.shape[3]%config.TRAIN.IMAGE_ALIGN!=0:
            new_height = math.ceil(float(im_tensor.shape[2])/config.TRAIN.IMAGE_ALIGN)*config.TRAIN.IMAGE_ALIGN
            new_width = math.ceil(float(im_tensor.shape[3])/config.TRAIN.IMAGE_ALIGN)*config.TRAIN.IMAGE_ALIGN
            new_im_tensor = np.zeros((1, 3, int(new_height), int(new_width)))
            new_im_tensor[:,:,0:im_tensor.shape[2],0:im_tensor.shape[3]] = im_tensor
            print(im_tensor.shape, new_im_tensor.shape, file=sys.stderr)
            im_tensor = new_im_tensor
        #print('boxes', new_rec['boxes'], file=sys.stderr)
        im_info = [im_tensor.shape[2], im_tensor.shape[3], im_scale]
        new_rec['im_info'] = im_info
        processed_roidb.append(new_rec)
    return processed_ims, processed_roidb

TMP_ID = -1
#bakup method
def __get_crop_image(roidb):
    """
    preprocess image and return processed roidb
    :param roidb: a list of roidb
    :return: list of img as in mxnet format
    roidb add new item['im_info']
    0 --- x (width, second dim of im)
    |
    y (height, first dim of im)
    """
    #roidb and each roi_rec can not be changed as it will be reused in next epoch
    num_images = len(roidb)
    processed_ims = []
    processed_roidb = []
    for i in range(num_images):
        roi_rec = roidb[i]
        if 'stream' in roi_rec:
          im = cv2.imdecode(roi_rec['stream'], cv2.IMREAD_COLOR)
        else:
          assert os.path.exists(roi_rec['image']), '{} does not exist'.format(roi_rec['image'])
          im = cv2.imread(roi_rec['image'])
        if roidb[i]['flipped']:
            im = im[:, ::-1, :]
        if 'boxes_mask' in roi_rec:
          #im = im.astype(np.float32)
          boxes_mask = roi_rec['boxes_mask'].copy()
          boxes_mask = boxes_mask.astype(np.int)
          for j in xrange(boxes_mask.shape[0]):
            m = boxes_mask[j]
            im[m[1]:m[3],m[0]:m[2],:] = 0
            #print('find mask', m, file=sys.stderr)
        new_rec = roi_rec.copy()


        #choose one gt randomly
        SIZE = config.SCALES[0][0]
        TARGET_BOX_SCALES = np.array([16,32,64,128,256,512])
        assert roi_rec['boxes'].shape[0]>0
        candidates = []
        for i in xrange(roi_rec['boxes'].shape[0]):
          box = roi_rec['boxes'][i]
          box_size = max(box[2]-box[0], box[3]-box[1])
          if box_size<config.TRAIN.MIN_BOX_SIZE:
            continue
          #if box[0]<0 or box[1]<0:
          #  continue
          #if box[2]>im.shape[1] or box[3]>im.shape[0]:
          #  continue;
          candidates.append(i)
        assert len(candidates)>0
        box_ind = random.choice(candidates)
        box = roi_rec['boxes'][box_ind]
        box_size = max(box[2]-box[0], box[3]-box[1])
        dist = np.abs(TARGET_BOX_SCALES - box_size)
        nearest = np.argmin(dist)
        target_ind = random.randrange(min(len(TARGET_BOX_SCALES), nearest+2))
        target_box_size = TARGET_BOX_SCALES[target_ind]
        im_scale = float(target_box_size) / box_size
        #min_scale = float(SIZE)/np.min(im.shape[0:2])
        #if im_scale<min_scale:
        #  im_scale = min_scale
        im = cv2.resize(im, None, None, fx=im_scale, fy=im_scale, interpolation=cv2.INTER_LINEAR)
        new_rec['boxes'] = roi_rec['boxes'].copy()*im_scale
        box_scale = new_rec['boxes'][box_ind].copy().astype(np.int)
        ul_min = box_scale[2:4] - SIZE
        ul_max = box_scale[0:2]
        assert ul_min[0]<=ul_max[0]
        assert ul_min[1]<=ul_max[1]
        #print('ul', ul_min, ul_max, box)
        up, left = np.random.randint(ul_min[1], ul_max[1]+1), np.random.randint(ul_min[0], ul_max[0]+1)
        #print('box', box, up, left)
        M = [ [1.0, 0.0, -left],
              [0.0, 1.0, -up], ]
        M = np.array(M)
        im = cv2.warpAffine(im, M, (SIZE, SIZE), borderValue = tuple(config.PIXEL_MEANS))
        #tbox = np.array([left, left+SIZE, up, up+SIZE], dtype=np.int)
        #im_new = np.zeros( (SIZE, SIZE,3), dtype=im.dtype)
        #for i in xrange(3):
        #  im_new[:,:,i] = config.PIXEL_MEANS[i]
        new_rec['boxes'][:,0] -= left
        new_rec['boxes'][:,2] -= left
        new_rec['boxes'][:,1] -= up
        new_rec['boxes'][:,3] -= up
        box_trans = new_rec['boxes'][box_ind].copy().astype(np.int)
        #print('sel box', im_scale, box, box_scale, box_trans, file=sys.stderr)
        #print('before', new_rec['boxes'].shape[0])
        boxes_new = []
        classes_new = []
        for i in xrange(new_rec['boxes'].shape[0]):
          box = new_rec['boxes'][i]
          box_size = max(box[2]-box[0], box[3]-box[1])
          center = np.array(([box[0], box[1]]+[box[2], box[3]]))/2
          if center[0]<0 or center[1]<0 or center[0]>=im.shape[1] or center[1]>=im.shape[0]:
            continue
          if box_size<config.TRAIN.MIN_BOX_SIZE:
            continue
          boxes_new.append(box)
          classes_new.append(new_rec['gt_classes'][i])
        new_rec['boxes'] = np.array(boxes_new)
        new_rec['gt_classes'] = np.array(classes_new)
        #print('after', new_rec['boxes'].shape[0])
        #assert new_rec['boxes'].shape[0]>0
        DEBUG = True
        if DEBUG:
          global TMP_ID
          if TMP_ID<10:
            tim = im.copy()
            for i in xrange(new_rec['boxes'].shape[0]):
              box = new_rec['boxes'][i].copy().astype(np.int)
              cv2.rectangle(tim, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 1)
            filename = './trainimages/train%d.png' % TMP_ID
            TMP_ID+=1
            cv2.imwrite(filename, tim)

        im_tensor = transform(im, config.PIXEL_MEANS, config.PIXEL_STDS, config.PIXEL_SCALE)

        processed_ims.append(im_tensor)
        #print('boxes', new_rec['boxes'], file=sys.stderr)
        im_info = [im_tensor.shape[2], im_tensor.shape[3], im_scale]
        new_rec['im_info'] = im_info
        processed_roidb.append(new_rec)
    return processed_ims, processed_roidb

def expand_bboxes(bboxes,
                  image_width,
                  image_height,
                  expand_left=2.,
                  expand_up=2.,
                  expand_right=2.,
                  expand_down=2.):
    """
    Expand bboxes, expand 2 times by defalut.
    """
    expand_boxes = []
    for bbox in bboxes:
        xmin = bbox[0]
        ymin = bbox[1]
        xmax = bbox[2]
        ymax = bbox[3]
        w = xmax - xmin
        h = ymax - ymin
        ex_xmin = max(xmin - w / expand_left, 0.)
        ex_ymin = max(ymin - h / expand_up, 0.)
        ex_xmax = min(xmax + w / expand_right, image_width)
        ex_ymax = min(ymax + h / expand_down, image_height)
        expand_boxes.append([ex_xmin, ex_ymin, ex_xmax, ex_ymax])
    return expand_boxes

def get_crop_image1(roidb):
    """
    preprocess image and return processed roidb
    :param roidb: a list of roidb
    :return: list of img as in mxnet format
    roidb add new item['im_info']
    0 --- x (width, second dim of im)
    |
    y (height, first dim of im)
    """
    #roidb and each roi_rec can not be changed as it will be reused in next epoch
    num_images = len(roidb)
    processed_ims = []
    processed_roidb = []
    for i in range(num_images):
        roi_rec = roidb[i]
        if 'stream' in roi_rec:
          im = cv2.imdecode(roi_rec['stream'], cv2.IMREAD_COLOR)
        else:
          assert os.path.exists(roi_rec['image']), '{} does not exist'.format(roi_rec['image'])
          im = cv2.imread(roi_rec['image'])
        if roidb[i]['flipped']:
            im = im[:, ::-1, :]
        if 'boxes_mask' in roi_rec:
          #im = im.astype(np.float32)
          boxes_mask = roi_rec['boxes_mask'].copy()
          boxes_mask = boxes_mask.astype(np.int)
          for j in xrange(boxes_mask.shape[0]):
            m = boxes_mask[j]
            im[m[1]:m[3],m[0]:m[2],:] = 127
            #print('find mask', m, file=sys.stderr)
        SIZE = config.SCALES[0][0]
        PRE_SCALES = [0.3, 0.45, 0.6, 0.8, 1.0]
        #PRE_SCALES = [0.3, 0.45, 0.6, 0.8, 1.0, 0.8, 1.0, 0.8, 1.0]
        _scale = random.choice(PRE_SCALES)
        #_scale = np.random.uniform(PRE_SCALES[0], PRE_SCALES[-1])
        size = int(np.min(im.shape[0:2])*_scale)
        #size = int(np.round(_scale*np.min(im.shape[0:2])))
        im_scale = float(SIZE)/size
        #origin_im_scale = im_scale
        #size = np.round(np.min(im.shape[0:2])*im_scale)
        #im_scale *= (float(SIZE)/size)
        origin_shape = im.shape
        if _scale>10.0: #avoid im.size<SIZE, never?
          sizex = int(np.round(im.shape[1]*im_scale))
          sizey = int(np.round(im.shape[0]*im_scale))
          if sizex<SIZE:
            sizex = SIZE
            print('keepx', sizex)
          if sizey<SIZE:
            sizey = SIZE
            print('keepy', sizex)
          im = cv2.resize(im, (sizex, sizey), interpolation=cv2.INTER_LINEAR)
        else:
          im = cv2.resize(im, None, None, fx=im_scale, fy=im_scale, interpolation=cv2.INTER_LINEAR)

        assert im.shape[0]>=SIZE and im.shape[1]>=SIZE
        #print('image size', origin_shape, _scale, SIZE, size, im_scale)

        new_rec = roi_rec.copy()
        new_rec['boxes'] = roi_rec['boxes'].copy() * im_scale
        if config.FACE_LANDMARK:
          new_rec['landmarks'] = roi_rec['landmarks'].copy()
          new_rec['landmarks'][:,:,0:2] *= im_scale
        retry = 0
        LIMIT = 25
        size = SIZE
        while retry<LIMIT:
          up, left = (np.random.randint(0, im.shape[0]-size+1), np.random.randint(0, im.shape[1]-size+1))
          boxes_new = new_rec['boxes'].copy()
          im_new = im[up:(up+size), left:(left+size), :]
          #print('crop', up, left, size, im_scale)
          boxes_new[:,0] -= left
          boxes_new[:,2] -= left
          boxes_new[:,1] -= up
          boxes_new[:,3] -= up
          if config.FACE_LANDMARK:
            landmarks_new = new_rec['landmarks'].copy()
            landmarks_new[:,:,0] -= left
            landmarks_new[:,:,1] -= up
            #for i in range(0,10,2):
            #  landmarks_new[:,i] -= left
            #for i in range(1,10,2):
            #  landmarks_new[:,i] -= up
            valid_landmarks = []
          #im_new = cv2.resize(im_new, (SIZE, SIZE), interpolation=cv2.INTER_LINEAR)
          #boxes_new *= im_scale
          #print(origin_shape, im_new.shape, im_scale)
          valid = []
          valid_boxes = []
          for i in xrange(boxes_new.shape[0]):
            box = boxes_new[i]
            #center = np.array(([box[0], box[1]]+[box[2], box[3]]))/2
            centerx = (box[0]+box[2])/2
            centery = (box[1]+box[3])/2

            #box[0] = max(0, box[0])
            #box[1] = max(0, box[1])
            #box[2] = min(im_new.shape[1], box[2])
            #box[3] = min(im_new.shape[0], box[3])
            box_size = max(box[2]-box[0], box[3]-box[1])

            if centerx<0 or centery<0 or centerx>=im_new.shape[1] or centery>=im_new.shape[0]:
              continue
            if box_size<config.TRAIN.MIN_BOX_SIZE:
              continue
            #filter by landmarks? TODO
            valid.append(i)
            valid_boxes.append(box)
            if config.FACE_LANDMARK:
              valid_landmarks.append(landmarks_new[i])
          if len(valid)>0 or retry==LIMIT-1:
            im = im_new
            new_rec['boxes'] = np.array(valid_boxes)
            new_rec['gt_classes'] = new_rec['gt_classes'][valid]
            if config.FACE_LANDMARK:
              new_rec['landmarks'] = np.array(valid_landmarks)
            if config.HEAD_BOX:
              face_box = new_rec['boxes']
              head_box = expand_bboxes(face_box, image_width=im.shape[1], image_height=im.shape[0])
              new_rec['boxes_head'] = np.array(head_box)
            break

          retry+=1

        if config.COLOR_MODE>0 and config.COLOR_JITTERING>0.0:
          im = im.astype(np.float32)
          im = color_aug(im, config.COLOR_JITTERING)

        #assert np.all(new_rec['landmarks'][:,10]>0.0)
        global TMP_ID
        if TMP_ID>=0 and TMP_ID<10:
          tim = im.copy().astype(np.uint8)
          for i in xrange(new_rec['boxes'].shape[0]):
            box = new_rec['boxes'][i].copy().astype(np.int)
            cv2.rectangle(tim, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 1)
            print('draw box:', box)
          if config.FACE_LANDMARK:
            for i in xrange(new_rec['landmarks'].shape[0]):
              landmark = new_rec['landmarks'][i].copy()
              if landmark[0][2]<0:
                print('zero', landmark)
                continue
              landmark = landmark.astype(np.int)
              print('draw landmark', landmark)
              for k in range(5):
                color = (0, 0, 255)
                if k==0 or k==3:
                  color = (0, 255, 0)
                pp = (landmark[k][0], landmark[k][1])
                cv2.circle(tim, (pp[0], pp[1]), 1, color, 2)
          filename = './trainimages/train%d.png' % TMP_ID
          print('write', filename)
          cv2.imwrite(filename, tim)
          TMP_ID+=1

        im_tensor = transform(im, config.PIXEL_MEANS, config.PIXEL_STDS, config.PIXEL_SCALE)

        processed_ims.append(im_tensor)
        #print('boxes', new_rec['boxes'], file=sys.stderr)
        im_info = [im_tensor.shape[2], im_tensor.shape[3], im_scale]
        new_rec['im_info'] = np.array(im_info, dtype=np.float32)
        processed_roidb.append(new_rec)
    return processed_ims, processed_roidb

def get_crop_image2(roidb):
    """
    preprocess image and return processed roidb
    :param roidb: a list of roidb
    :return: list of img as in mxnet format
    roidb add new item['im_info']
    0 --- x (width, second dim of im)
    |
    y (height, first dim of im)
    """
    #roidb and each roi_rec can not be changed as it will be reused in next epoch
    num_images = len(roidb)
    processed_ims = []
    processed_roidb = []
    for i in range(num_images):
        roi_rec = roidb[i]
        if 'stream' in roi_rec:
          im = cv2.imdecode(roi_rec['stream'], cv2.IMREAD_COLOR)
        else:
          assert os.path.exists(roi_rec['image']), '{} does not exist'.format(roi_rec['image'])
          im = cv2.imread(roi_rec['image'])
        if roidb[i]['flipped']:
            im = im[:, ::-1, :]
        if 'boxes_mask' in roi_rec:
          #im = im.astype(np.float32)
          boxes_mask = roi_rec['boxes_mask'].copy()
          boxes_mask = boxes_mask.astype(np.int)
          for j in xrange(boxes_mask.shape[0]):
            m = boxes_mask[j]
            im[m[1]:m[3],m[0]:m[2],:] = 0
            #print('find mask', m, file=sys.stderr)
        SIZE = config.SCALES[0][0]
        scale_array = np.array([16,32,64,128,256,512], dtype=np.float32)
        candidates = []
        for i in xrange(roi_rec['boxes'].shape[0]):
          box = roi_rec['boxes'][i]
          box_size = max(box[2]-box[0], box[3]-box[1])
          if box_size<config.TRAIN.MIN_BOX_SIZE:
            continue
          #if box[0]<0 or box[1]<0:
          #  continue
          #if box[2]>im.shape[1] or box[3]>im.shape[0]:
          #  continue;
          candidates.append(i)
        assert len(candidates)>0
        box_ind = random.choice(candidates)
        box = roi_rec['boxes'][box_ind]
        width = box[2]-box[0]
        height = box[3]-box[1]
        wid = width
        hei = height
        resize_width, resize_height = config.SCALES[0]
        image_width = im.shape[0]
        image_height = im.shape[1]
        area = width*height
        range_size = 0
        for scale_ind in range(0, len(scale_array) - 1):
            if area > scale_array[scale_ind] ** 2 and area < \
                    scale_array[scale_ind + 1] ** 2:
                range_size = scale_ind + 1
                break

        if area > scale_array[len(scale_array) - 2]**2:
            range_size = len(scale_array) - 2
        scale_choose = 0.0
        if range_size == 0:
            rand_idx_size = 0
        else:
            # np.random.randint range: [low, high)
            rng_rand_size = np.random.randint(0, range_size + 1)
            rand_idx_size = rng_rand_size % (range_size + 1)

        if rand_idx_size == range_size:
            min_resize_val = scale_array[rand_idx_size] / 2.0
            max_resize_val = min(2.0 * scale_array[rand_idx_size],
                                 2 * math.sqrt(wid * hei))
            scale_choose = random.uniform(min_resize_val, max_resize_val)
        else:
            min_resize_val = scale_array[rand_idx_size] / 2.0
            max_resize_val = 2.0 * scale_array[rand_idx_size]
            scale_choose = random.uniform(min_resize_val, max_resize_val)

        sample_bbox_size = wid * resize_width / scale_choose

        w_off_orig = 0.0
        h_off_orig = 0.0
        if sample_bbox_size < max(image_height, image_width):
            if wid <= sample_bbox_size:
                w_off_orig = np.random.uniform(xmin + wid - sample_bbox_size,
                                               xmin)
            else:
                w_off_orig = np.random.uniform(xmin,
                                               xmin + wid - sample_bbox_size)

            if hei <= sample_bbox_size:
                h_off_orig = np.random.uniform(ymin + hei - sample_bbox_size,
                                               ymin)
            else:
                h_off_orig = np.random.uniform(ymin,
                                               ymin + hei - sample_bbox_size)

        else:
            w_off_orig = np.random.uniform(image_width - sample_bbox_size, 0.0)
            h_off_orig = np.random.uniform(image_height - sample_bbox_size, 0.0)

        w_off_orig = math.floor(w_off_orig)
        h_off_orig = math.floor(h_off_orig)

        # Figure out top left coordinates.
        w_off = 0.0
        h_off = 0.0
        w_off = float(w_off_orig / image_width)
        h_off = float(h_off_orig / image_height)
        im_new = im[up:(up+size), left:(left+size), :]

        sampled_bbox = bbox(w_off, h_off,
                            w_off + float(sample_bbox_size / image_width),
                            h_off + float(sample_bbox_size / image_height))
        return sampled_bbox

        box_size = max(box[2]-box[0], box[3]-box[1])
        dist = np.abs(TARGET_BOX_SCALES - box_size)
        nearest = np.argmin(dist)
        target_ind = random.randrange(min(len(TARGET_BOX_SCALES), nearest+2))
        target_box_size = TARGET_BOX_SCALES[target_ind]
        im_scale = float(target_box_size) / box_size
        PRE_SCALES = [0.3, 0.45, 0.6, 0.8, 1.0]
        _scale = random.choice(PRE_SCALES)
        #_scale = np.random.uniform(PRE_SCALES[0], PRE_SCALES[-1])
        size = int(np.round(_scale*np.min(im.shape[0:2])))
        im_scale = float(SIZE)/size
        #origin_im_scale = im_scale
        #size = np.round(np.min(im.shape[0:2])*im_scale)
        #im_scale *= (float(SIZE)/size)
        origin_shape = im.shape
        if _scale>10.0: #avoid im.size<SIZE, never?
          sizex = int(np.round(im.shape[1]*im_scale))
          sizey = int(np.round(im.shape[0]*im_scale))
          if sizex<SIZE:
            sizex = SIZE
            print('keepx', sizex)
          if sizey<SIZE:
            sizey = SIZE
            print('keepy', sizex)
          im = cv2.resize(im, (sizex, sizey), interpolation=cv2.INTER_LINEAR)
        else:
          im = cv2.resize(im, None, None, fx=im_scale, fy=im_scale, interpolation=cv2.INTER_LINEAR)
        assert im.shape[0]>=SIZE and im.shape[1]>=SIZE

        new_rec = roi_rec.copy()
        new_rec['boxes'] = roi_rec['boxes'].copy() * im_scale
        if config.FACE_LANDMARK:
          new_rec['landmarks'] = roi_rec['landmarks'].copy() * im_scale
        retry = 0
        LIMIT = 25
        size = SIZE
        while retry<LIMIT:
          up, left = (np.random.randint(0, im.shape[0]-size+1), np.random.randint(0, im.shape[1]-size+1))
          boxes_new = new_rec['boxes'].copy()
          im_new = im[up:(up+size), left:(left+size), :]
          #print('crop', up, left, size, im_scale)
          boxes_new[:,0] -= left
          boxes_new[:,2] -= left
          boxes_new[:,1] -= up
          boxes_new[:,3] -= up
          if config.FACE_LANDMARK:
            landmarks_new = new_rec['landmarks'].copy()
            for i in range(0,10,2):
              landmarks_new[:,i] -= left
            for i in range(1,10,2):
              landmarks_new[:,i] -= up
            valid_landmarks = []
          #im_new = cv2.resize(im_new, (SIZE, SIZE), interpolation=cv2.INTER_LINEAR)
          #boxes_new *= im_scale
          #print(origin_shape, im_new.shape, im_scale)
          valid = []
          valid_boxes = []
          for i in xrange(boxes_new.shape[0]):
            box = boxes_new[i]
            #center = np.array(([box[0], box[1]]+[box[2], box[3]]))/2
            centerx = (box[0]+box[2])/2
            centery = (box[1]+box[3])/2

            #box[0] = max(0, box[0])
            #box[1] = max(0, box[1])
            #box[2] = min(im_new.shape[1], box[2])
            #box[3] = min(im_new.shape[0], box[3])
            box_size = max(box[2]-box[0], box[3]-box[1])

            if centerx<0 or centery<0 or centerx>=im_new.shape[1] or centery>=im_new.shape[0]:
              continue
            if box_size<config.TRAIN.MIN_BOX_SIZE:
              continue
            #filter by landmarks? TODO
            valid.append(i)
            valid_boxes.append(box)
            if config.FACE_LANDMARK:
              valid_landmarks.append(landmarks_new[i])
          if len(valid)>0 or retry==LIMIT-1:
            im = im_new
            new_rec['boxes'] = np.array(valid_boxes)
            new_rec['gt_classes'] = new_rec['gt_classes'][valid]
            if config.FACE_LANDMARK:
              new_rec['landmarks'] = np.array(valid_landmarks)
            break

          retry+=1

        if config.COLOR_JITTERING>0.0:
          im = im.astype(np.float32)
          im = color_aug(im, config.COLOR_JITTERING)

        #assert np.all(new_rec['landmarks'][:,10]>0.0)
        global TMP_ID
        if TMP_ID>=0 and TMP_ID<10:
          tim = im.copy().astype(np.uint8)
          for i in xrange(new_rec['boxes'].shape[0]):
            box = new_rec['boxes'][i].copy().astype(np.int)
            cv2.rectangle(tim, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 1)
            print('draw box:', box)
          if config.FACE_LANDMARK:
            for i in xrange(new_rec['landmarks'].shape[0]):
              landmark = new_rec['landmarks'][i].copy()
              if landmark[10]==0.0:
                print('zero', landmark)
                continue
              landmark = landmark.astype(np.int)
              print('draw landmark', landmark)
              for k in range(5):
                color = (0, 0, 255)
                if k==0 or k==3:
                  color = (0, 255, 0)
                pp = (landmark[k*2], landmark[1+k*2])
                cv2.circle(tim, (pp[0], pp[1]), 1, color, 2)
          filename = './trainimages/train%d.png' % TMP_ID
          print('write', filename)
          cv2.imwrite(filename, tim)
          TMP_ID+=1

        im_tensor = transform(im, config.PIXEL_MEANS, config.PIXEL_STDS, config.PIXEL_SCALE)

        processed_ims.append(im_tensor)
        #print('boxes', new_rec['boxes'], file=sys.stderr)
        im_info = [im_tensor.shape[2], im_tensor.shape[3], im_scale]
        new_rec['im_info'] = np.array(im_info, dtype=np.float32)
        processed_roidb.append(new_rec)
    return processed_ims, processed_roidb

def do_mixup(im1, roidb1, im2, roidb2):
  im = (im1+im2)/2.0
  roidb = {}
  #print(roidb1.keys())
  #for k in roidb1:
  for k in ['boxes', 'landmarks', 'gt_classes', 'im_info']:
    v1 = roidb1[k]
    v2 = roidb2[k]
    if k!='im_info':
      #print('try', k, v1.shape, v2.shape)
      if v1.shape[0]>0 and v2.shape[0]>0:
        v = np.concatenate( (v1, v2), axis=0 )
      else:
        v = v1
    else:
      v = v1
    #print(k, v1.shape, v2.shape, v.shape)
    roidb[k] = v
  return im, roidb

def get_crop_image(roidb):
    ims, roidbs = get_crop_image1(roidb)
    # if config.ct_reproduce:
    #     ims, roidbs = get_image(roidb)
    if config.MIXUP>0.0 and np.random.random()<config.MIXUP:
      for i in range(len(ims)):
        im = ims[i]
        roidb = roidbs[i]
        j = np.random.randint(0, len(ims)-1)
        if j>=i:
          j+=1
        im, roidb = do_mixup(im, roidb, ims[j], roidbs[j])
        ims[i] = im
        roidbs[i] = roidb
    return ims, roidbs

def resize(im, target_size, max_size, stride=0, min_size=0):
    """
    only resize input image to target size and return scale
    :param im: BGR image input by opencv
    :param target_size: one dimensional size (the short side)
    :param max_size: one dimensional max size (the long side)
    :param stride: if given, pad the image to designated stride
    :return:
    """
    im_shape = im.shape
    im_size_min = np.min(im_shape[0:2])
    im_size_max = np.max(im_shape[0:2])
    im_scale = float(target_size) / float(im_size_min)
    # prevent bigger axis from being more than max_size:
    if np.round(im_scale * im_size_max) > max_size:
        im_scale = float(max_size) / float(im_size_max)
        if min_size>0 and np.round(im_scale*im_size_min)<min_size:
          im_scale = float(min_size) / float(im_size_min)
    im = cv2.resize(im, None, None, fx=im_scale, fy=im_scale, interpolation=cv2.INTER_LINEAR)

    if stride == 0:
        return im, im_scale
    else:
        # pad to product of stride
        im_height = int(np.ceil(im.shape[0] / float(stride)) * stride)
        im_width = int(np.ceil(im.shape[1] / float(stride)) * stride)
        im_channel = im.shape[2]
        padded_im = np.zeros((im_height, im_width, im_channel))
        padded_im[:im.shape[0], :im.shape[1], :] = im
        return padded_im, im_scale


def transform(im, pixel_means, pixel_stds, pixel_scale):
    """
    transform into mxnet tensor,
    subtract pixel size and transform to correct format
    :param im: [height, width, channel] in BGR
    :param pixel_means: [B, G, R pixel means]
    :return: [batch, channel, height, width]
    """
    im_tensor = np.zeros((1, 3, im.shape[0], im.shape[1]))
    for i in range(3):
        im_tensor[0, i, :, :] = (im[:, :, 2 - i]/pixel_scale - pixel_means[2 - i]) / pixel_stds[2 - i]
    return im_tensor


def transform_inverse(im_tensor, pixel_means):
    """
    transform from mxnet im_tensor to ordinary RGB image
    im_tensor is limited to one image
    :param im_tensor: [batch, channel, height, width]
    :param pixel_means: [B, G, R pixel means]
    :return: im [height, width, channel(RGB)]
    """
    assert im_tensor.shape[0] == 1
    im_tensor = im_tensor.copy()
    # put channel back
    channel_swap = (0, 2, 3, 1)
    im_tensor = im_tensor.transpose(channel_swap)
    im = im_tensor[0]
    assert im.shape[2] == 3
    im += pixel_means[[2, 1, 0]]
    im = im.astype(np.uint8)
    return im


def tensor_vstack(tensor_list, pad=0):
    """
    vertically stack tensors
    :param tensor_list: list of tensor to be stacked vertically
    :param pad: label to pad with
    :return: tensor with max shape
    """
    ndim = len(tensor_list[0].shape)
    dtype = tensor_list[0].dtype
    islice = tensor_list[0].shape[0]
    dimensions = []
    first_dim = sum([tensor.shape[0] for tensor in tensor_list])
    dimensions.append(first_dim)
    for dim in range(1, ndim):
        dimensions.append(max([tensor.shape[dim] for tensor in tensor_list]))
    if pad == 0:
        all_tensor = np.zeros(tuple(dimensions), dtype=dtype)
    elif pad == 1:
        all_tensor = np.ones(tuple(dimensions), dtype=dtype)
    else:
        all_tensor = np.full(tuple(dimensions), pad, dtype=dtype)
    if ndim == 1:
        for ind, tensor in enumerate(tensor_list):
            all_tensor[ind*islice:(ind+1)*islice] = tensor
    elif ndim == 2:
        for ind, tensor in enumerate(tensor_list):
            all_tensor[ind*islice:(ind+1)*islice, :tensor.shape[1]] = tensor
    elif ndim == 3:
        for ind, tensor in enumerate(tensor_list):
            all_tensor[ind*islice:(ind+1)*islice, :tensor.shape[1], :tensor.shape[2]] = tensor
    elif ndim == 4:
        for ind, tensor in enumerate(tensor_list):
            all_tensor[ind*islice:(ind+1)*islice, :tensor.shape[1], :tensor.shape[2], :tensor.shape[3]] = tensor
    elif ndim == 5:
        for ind, tensor in enumerate(tensor_list):
            all_tensor[ind*islice:(ind+1)*islice, :tensor.shape[1], :tensor.shape[2], :tensor.shape[3], :tensor.shape[4]] = tensor
    else:
        print(tensor_list[0].shape)
        raise Exception('Sorry, unimplemented.')
    return all_tensor

