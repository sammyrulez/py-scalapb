# Python ScalaPB Communication Library

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-Apache%202.0-blue)

The **Python ScalaPB Communication Library** is an open-source Python package that simplifies communication with services using [ScalaPB](https://scalapb.github.io/) for Protocol Buffers (Protobuf) serialization. This library provides a straightforward way to interact with ScalaPB-based services, making it easier to integrate your Python applications with services written in Scala.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

You can install the Python ScalaPB Communication Library using `pip`. Simply run:

```bash
pip install py-scalapb
```

## Usage

If you are using the protoc compiler to generate code from Protobuf files with ScalaPB dependencies, you may encounter a "scalapb module not found" issue. Adding this library to your project can help solve this problem.

```python
from scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2
```

## Contributing

We welcome contributions from the open-source community. To contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and write tests if necessary.
4. Ensure that your code follows the project's coding style and guidelines.
5. Submit a pull request.

Please make sure to provide a detailed description of the changes you've made, along with clear commit messages.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
