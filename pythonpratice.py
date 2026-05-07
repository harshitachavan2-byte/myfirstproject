{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM4pj3GLaTlAW/ej1bArlhc",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/harshitachavan2-byte/myfirstproject/blob/main/Untitled0.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YkcnF1ycglz2",
        "outputId": "034ef588-2736-4f5a-f9ba-cbb9f76e2045"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello world\n"
          ]
        }
      ],
      "source": [
        "print(\"Hello world\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Harshita\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XsMB-Fjsg85L",
        "outputId": "3953f1f0-309a-428b-ff39-9a7e1fa914cb"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Harshita\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name = str(input(\"Enter your name:\"))\n",
        "print(name)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-YOiQiZghRSy",
        "outputId": "81336d68-415d-4a96-edfb-0db01aa8feca"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your name:harshita\n",
            "harshita\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = 5\n",
        "b = 3\n",
        "sum = a + b\n",
        "print(sum)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0MaFz2h-hiiP",
        "outputId": "cade3fe0-8f17-4a10-8903-2007e1bc2076"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "8\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = int(input(\"enter the num:\"))\n",
        "square_n = n ** 2\n",
        "print(\"Square is\", square_n)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IZ4GUGEMh5FD",
        "outputId": "5bc5f5d7-92bd-433d-b963-84edb6f127c1"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter the num:4\n",
            "Square is 16\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Area = Length * Breath\n",
        "L = 5\n",
        "B = 4\n",
        "Area = L * B\n",
        "print(\"Area of Rectangle:\", Area)\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xh4zOF6Vj6q0",
        "outputId": "236717b4-bbdf-455a-ab11-300ef5d8256a"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Area of Rectangle: 20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = 44\n",
        "b = 80\n",
        "c = 59\n",
        "Avg = (a + b + c)/ 3\n",
        "print(\"Average Is:\", Avg)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oLv9zN0wmEX2",
        "outputId": "4bb26f03-1305-417c-aefe-8c399726a154"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Average Is: 61.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = int(input (\"Enter the Num:\"))\n",
        "cube = n**3\n",
        "print (\"Cube =:\", cube)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Vi-naes6mirZ",
        "outputId": "b3210ded-9e0e-46f1-b46d-8b3797b184ae"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the Num:3\n",
            "Cube =: 27\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n = int(input(\"enter the number:\"))\n",
        "seconds = n * 60\n",
        "print(\"seconds=:\", seconds)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CjutQuHjnD-d",
        "outputId": "2c74bb0f-d856-4b28-99eb-6ccbd4b0a96f"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter the number:5\n",
            "seconds=: 300\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "l = 12\n",
        "b = 9\n",
        "perimeter = 2* (l + b)\n",
        "print(\"perimeter =:\", perimeter)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mD8p3gjLn9WJ",
        "outputId": "c1600c8a-1841-49a8-e4b6-08c1810a83e7"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "perimeter =: 42\n"
          ]
        }
      ]
    }
  ]
}
