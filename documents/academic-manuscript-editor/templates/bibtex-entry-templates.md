# BibTeX Entry Templates

These templates define output structure for normalized bibliography export.

## General Rules
- Use stable citation keys.
- Keep one field per line.
- Prefer DOI over URL when both exist, but keep URL for online-first sources.
- Preserve braces for terms requiring case protection.

## Book
```bibtex
@book{key,
  author    = {Author, A.},
  title     = {Title},
  edition   = {2},
  year      = {2022},
  publisher = {Publisher},
  address   = {City},
  isbn      = {978-0-000000-00-0},
  doi       = {10.0000/example}
}
```

## Article
```bibtex
@article{key,
  author       = {Author, A. and Author, B.},
  title        = {Article Title},
  journal      = {Journal Name},
  year         = {2024},
  volume       = {18},
  number       = {2},
  pages        = {101--120},
  doi          = {10.0000/example},
  url          = {https://example.org/article}
}
```

## InProceedings
```bibtex
@inproceedings{key,
  author    = {Author, A.},
  title     = {Paper Title},
  booktitle = {Conference Title},
  year      = {2023},
  pages     = {55--68},
  publisher = {Publisher},
  doi       = {10.0000/example}
}
```

## Thesis
```bibtex
@phdthesis{key,
  author = {Author, A.},
  title  = {Thesis Title},
  school = {University Name},
  year   = {2021},
  type   = {PhD thesis}
}
```

## Online

    @misc{key,
      author       = {Organization Name},
      title        = {Resource Title},
      year         = {2025},
      howpublished = {\url{https://example.org/resource}},
      note         = {Accessed: 2026-05-25}
    }

