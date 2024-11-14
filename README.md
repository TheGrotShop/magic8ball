<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/TheGrotShop/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/thegrotshop/black-and-white-circle-256.png" alt="TheGrotShop logo" />
    </a>
    <br />
    <a href="https://github.com/TheGrotShop/magic-8ball/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/TheGrotShop/magic-8ball/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/TheGrotShop/magic-8ball/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/TheGrotShop/magic-8ball?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/TheGrotShop/magic-8ball">
        <img src="https://img.shields.io/github/created-at/TheGrotShop/magic-8ball?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/TheGrotShop/magic-8ball/releases/latest">
        <img src="https://img.shields.io/github/v/release/TheGrotShop/magic-8ball?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/TheGrotShop/magic-8ball/releases/latest">
        <img src="https://img.shields.io/github/release-date/TheGrotShop/magic-8ball?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/TheGrotShop/magic-8ball/releases/latest">
        <img src="https://img.shields.io/github/commits-since/TheGrotShop/magic-8ball/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/TheGrotShop/magic-8ball/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/TheGrotShop/magic-8ball/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/TheGrotShop/magic-8ball/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/TheGrotShop/magic-8ball/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

## Overview

`Magic 8-Ball` is a Python package that emulates the classic Magic 8-Ball toy, providing randomized responses to yes-or-no questions. This package is
designed to be both interactive and usable in various applications, allowing developers to integrate a fun, nostalgic feature into their projects.

## Features

- 20 traditional Magic 8-Ball responses (positive, neutral, and negative).
- Simple API to ask questions and get a response.
- Custom error handling for invalid inputs.
- Includes comprehensive test coverage.

## Installation

```bash
pip install wolfsoftware.magic8ball
```

## Usage

### Basic Example

Once installed, you can use the Magic 8-Ball package in your Python code.

```python
from wolfsoftware.magic8ball import Magic8Ball

# Create an instance of Magic8Ball
magic_ball = Magic8Ball()

# Ask a yes/no question
response = magic_ball.ask_question("Will it rain tomorrow?")
print("Magic 8-Ball says:", response)
```

### Handling Errors

The `ask_question` method raises an `InvalidQuestionError` if the question provided is not a non-empty string. Make sure to validate the input or handle
this exception as shown:

```python
from wolfsoftware.magic8ball import Magic8Ball, InvalidQuestionError

magic_ball = Magic8Ball()

try:
    response = magic_ball.ask_question("Will I get a promotion?")
    print("Magic 8-Ball says:", response)
except InvalidQuestionError as e:
    print("Error:", e)
```

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
