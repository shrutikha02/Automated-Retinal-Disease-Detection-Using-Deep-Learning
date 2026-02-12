# Automated Retinal Disease Detection using Deep Learning

## Overview

This project develops a deep learning-based clinical decision support system to automatically detect retinal diseases from Optical Coherence Tomography (OCT) images.

The model classifies images into four categories:

- CNV (Choroidal Neovascularization)
- DME (Diabetic Macular Edema)
- Drusen (Early Age-Related Macular Degeneration)
- Normal Retina

The system is designed to assist ophthalmologists by providing fast and consistent predictions.

---

## Problem Statement

Manual diagnosis of retinal diseases using OCT scans:

- Is time-consuming
- Requires trained specialists
- Can vary between doctors
- Is difficult in resource-limited regions

There is a need for an automated, scalable AI-based solution that can support early detection and triage.

---

## Solution Approach

The system uses transfer learning with MobileNetV3Large, a lightweight convolutional neural network architecture.

### Pipeline:

1. Load and preprocess OCT images
2. Resize to 224x224 resolution
3. Apply ImageNet normalization
4. Use pre-trained MobileNetV3Large
5. Add custom Dense layer for 4-class classification
6. Train using categorical cross-entropy loss

---

## Model Details

- Framework: TensorFlow / Keras
- Base Model: MobileNetV3Large (ImageNet pre-trained)
- Input Shape: 224 x 224 x 3
- Output: 4-class softmax
- Optimizer: Adam (learning rate = 1e-4)
- Epochs: 15
- Batch Size: 32
- Total Parameters: ~5.5 Million
- Model Size: ~21 MB

---

## Dataset

The dataset consists of OCT retinal images across four disease categories.

| Dataset | Total Images |
|----------|--------------|
| Training | 76,515 |
| Validation | 21,861 |

Images are organized into class-specific folders for supervised learning.

(Note: Dataset not included due to size and medical usage restrictions.)

---

## Inference Example

Example output prediction:

Input: DRUSEN-1112835-7.jpeg  
Confidence Scores:  
[0.0735, 0.0144, 0.8707, 0.0414]

Predicted Class: DRUSEN (87.07% confidence)

Inference time per image: < 1 second

---

## Clinical Recommendation Engine

The system integrates a rule-based recommendation module:

- CNV → Retinal specialist referral + Anti-VEGF therapy
- DME → Diabetes management + retinal therapy
- Drusen → AREDS2 supplements + monitoring
- Normal → Routine follow-up

This enhances the practical usability of the model in clinical workflows.

---

## Key Contributions

- Efficient transfer learning implementation
- Large-scale dataset handling
- Lightweight deployable architecture
- Clinical decision support integration
- Scalable solution for resource-limited settings

---

## Limitations

- Limited to four disease categories
- Performance depends on image quality
- No explainability module implemented yet

---

## Future Improvements

- Grad-CAM visualization
- Multi-modal imaging (Fundus + OCT)
- Severity grading
- Mobile deployment
- Ensemble modeling

---

## Author

Shruti Khaklary  
ACC HPC Program  
C-DAC CINE, IIT Guwahati Research Park

---

## License

For academic and research purposes only.
