# 30MHz case study in web performance – Replication package

This repository contains the replication package and dataset of the 30MHz case study on web performance. Using this repo, one can generate performance benchmark results for any web page, or replicate the results of the case study, as well as its statistical analysis.

This study has been designed, developed, and reported by the following investigators:

- [Jasper van Riet](https://jaspervanriet.nl) (Vrije Universiteit Amsterdam, 30MHz)
- [Ivano Malavolta](https://www.ivanomalavolta.com) (Vrije Universiteit Amsterdam)
- [Flavia Paganelli](https://nl.linkedin.com/in/flaviapaganelli) (30MHz)

For any information, interested researchers can contact us by sending an email to any of the investigators listed above.
The full dataset including raw data, performance benchmarking tools, and analysis scripts produced during the study are available below.

## How to cite the dataset
If the dataset or the results of our study are helping your research, consider to cite our study as follows, thanks!

```
@inproceedings{ICSME_2020,
  author    = {Jasper van Riet and Flavia Paganelli and Ivano Malavolta},
  title     = {{From 6.2 to 0.15 seconds - an Industrial Case Study on Mobile Web Performance}},
  booktitle = {{IEEE} International Conference on Software Maintenance and Evolution,
               {(ICSME)}},
  pages     = {to appear},
  year      = {2020},
  url       = {https://github.com/S2-group/ICSME-2020-replication-package/blob/master/ICSME_2020.pdf}
}
```

### Overview of the replication package
---

This replication package is structured as follows:

- Performance benchmarking tools can be found in the `metrics` and `metrics-ff` folders, for Chrome and Firefox respectively. The results can be found in `results`. The first result is the baseline situation.
- Analysis scripts and the raw data can be found in the `analyze` and `network` folders
- User study results, the app used, the experiment guide given to participants, and the analysis scripts can be found in the `userstudy` and `userstudy-tools` folders


## License

This software is licensed under the MIT License.

```
Copyright (c) 2020 Jasper van Riet

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
