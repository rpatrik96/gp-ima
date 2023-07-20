---

<div align="center">    
 
# Independent mechanisms in GPLVMs

<!--  
[//]: # ([![Paper]&#40;http://img.shields.io/badge/paper-arxiv.2206.02416-B31B1B.svg&#41;]&#40;https://arxiv.org/abs/2206.02416&#41;)

[//]: # ([![Conference]&#40;http://img.shields.io/badge/NeurIPS-2019-4b44ce.svg&#41;]&#40;https://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018&#41;)

[//]: # ([![Conference]&#40;http://img.shields.io/badge/ICLR-2019-4b44ce.svg&#41;]&#40;https://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018&#41;)

[//]: # ([![Conference]&#40;http://img.shields.io/badge/AnyConference-year-4b44ce.svg&#41;]&#40;https://papers.nips.cc/book/advances-in-neural-information-processing-systems-31-2018&#41;  )

[![Paper](http://img.shields.io/badge/arxiv-stat.ML:2206.02416-B31B1B.svg)](https://arxiv.org/abs/2206.02416)
-->  
[![Conference](http://img.shields.io/badge/AABI-2023.svg)](https://openreview.net/forum?id=WgK0RYP-6H)

![CI testing](https://github.com/rpatrik96/gp-ima/workflows/CI%20testing/badge.svg?branch=main&event=push)

<!-- 
[![DOI](https://zenodo.org/badge/431811003.svg)](https://zenodo.org/badge/latestdoi/431811003)
-->  

<!--  
Conference   
-->   
</div>
 
## Description   
We show that most common kernel choices in GPLVM restrict the functions (even in the prior) to the IMA class [(Gresele et al., 2021)](https://proceedings.neurips.cc/paper_files/paper/2021/hash/edc27f139c3b4e4bb29d1cdbc45663f9-Abstract.html), which shows that IMA is more prevalent in variational inference, even beyond VAEs [(Reizinger et al., 2022)](https://proceedings.neurips.cc/paper_files/paper/2022/hash/4eb91efe090f72f7cf42c69aab03fe85-Abstract-Conference.html).

## How to run   
First, install dependencies   
```bash
# clone gp-ima   
git clone --recurse-submodules https://github.com/rpatrik96/gp-ima


# install gp-ima   
cd gp-ima
pip install -e .   
pip install -r requirements.txt



# install submodule requirements
pip install --requirement tests/requirements.txt --quiet

# install pre-commit hooks (only necessary for development)
pre-commit install
 ```   



## Citation   

```

@inproceedings{
reizinger2023independent,
title={Independent Mechanism Analysis in {GPLVM}s},
author={Patrik Reizinger and Han-Bo Li and Aditya Ravuri and Ferenc Husz{\'a}r and Neil D Lawrence},
booktitle={Fifth Symposium on Advances in Approximate Bayesian Inference},
year={2023},
url={https://openreview.net/forum?id=WgK0RYP-6H}
}

```   
