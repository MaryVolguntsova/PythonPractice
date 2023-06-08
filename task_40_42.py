{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPbYAuUhDsDrquFIuPapka0",
      "include_colab_link": True
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
        "<a href=\"https://colab.research.google.com/github/Yulia74/Python_homework/blob/main/Homework_09.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)"
      ],
      "metadata": {
        "id": "5ULHtw_noJ6o"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd"
      ],
      "metadata": {
        "id": "BUc16wsgoOzz"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv('sample_data/california_housing_train.csv')"
      ],
      "metadata": {
        "id": "Dc22MzKconYy"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.query('population < = 500')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "UJey8gpWsz6k",
        "outputId": "dc7ae2fb-9b57-4620-a2a2-fb823f1c4c18"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              " longitude latitude housing_median_age total_rooms total_bedrooms \\\n",
              "2 -114.56 33.69 17.0 720.0 174.0 \n",
              "7 -114.59 34.83 41.0 812.0 168.0 \n",
              "17 -114.65 32.79 21.0 44.0 33.0 \n",
              "19 -114.67 33.92 17.0 97.0 24.0 \n",
              "21 -114.73 33.43 24.0 796.0 243.0 \n",
              "... ... ... ... ... ... \n",
              "16944 -124.14 40.67 23.0 580.0 117.0 \n",
              "16951 -124.15 40.81 50.0 340.0 74.0 \n",
              "16969 -124.17 40.80 52.0 661.0 316.0 \n",
              "16982 -124.18 40.62 35.0 952.0 178.0 \n",
              "16994 -124.25 40.28 32.0 1430.0 419.0 \n",
              "\n",
              " population households median_income median_house_value \n",
              "2 333.0 117.0 1.6509 85700.0 \n",
              "7 375.0 158.0 1.7083 48500.0 \n",
              "17 64.0 27.0 0.8571 25000.0 \n",
              "19 29.0 15.0 1.2656 27500.0 \n",
              "21 227.0 139.0 0.8964 59200.0 \n",
              "... ... ... ... ... \n",
              "16944       320.0       109.0         4.2054            130600.0  \n",
              "16951       235.0        83.0         1.7500             67500.0  \n",
              "16969       392.0       244.0         0.9570             60000.0  \n",
              "16982       480.0       179.0         3.0536            107000.0  \n",
              "16994       434.0       187.0         1.9417             76100.0  \n",
              "\n",
              "[1605 rows x 9 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-2a01e78d-57b1-4dd5-9c23-5d992b671f12\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>longitude</th>\n",
              "      <th>latitude</th>\n",
              "      <th>housing_median_age</th>\n",
              "      <th>total_rooms</th>\n",
              "      <th>total_bedrooms</th>\n",
              "      <th>population</th>\n",
              "      <th>households</th>\n",
              "      <th>median_income</th>\n",
              "      <th>median_house_value</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>-114.56</td>\n",
              "      <td>33.69</td>\n",
              "      <td>17.0</td>\n",
              "      <td>720.0</td>\n",
              "      <td>174.0</td>\n",
              "      <td>333.0</td>\n",
              "      <td>117.0</td>\n",
              "      <td>1.6509</td>\n",
              "      <td>85700.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>-114.59</td>\n",
              "      <td>34.83</td>\n",
              "      <td>41.0</td>\n",
              "      <td>812.0</td>\n",
              "      <td>168.0</td>\n",
              "      <td>375.0</td>\n",
              "      <td>158.0</td>\n",
              "      <td>1.7083</td>\n",
              "      <td>48500.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>17</th>\n",
              "      <td>-114.65</td>\n",
              "      <td>32.79</td>\n",
              "      <td>21.0</td>\n",
              "      <td>44.0</td>\n",
              "      <td>33.0</td>\n",
              "      <td>64.0</td>\n",
              "      <td>27.0</td>\n",
              "      <td>0.8571</td>\n",
              "      <td>25000.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19</th>\n",
              "      <td>-114.67</td>\n",
              "      <td>33.92</td>\n",
              "      <td>17.0</td>\n",
              "      <td>97.0</td>\n",
              "      <td>24.0</td>\n",
              "      <td>29.0</td>\n",
              "      <td>15.0</td>\n",
              "      <td>1.2656</td>\n",
              "      <td>27500.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>21</th>\n",
              "      <td>-114.73</td>\n",
              "      <td>33.43</td>\n",
              "      <td>24.0</td>\n",
              "      <td>796.0</td>\n",
              "      <td>243.0</td>\n",
              "      <td>227.0</td>\n",
              "      <td>139.0</td>\n",
              "      <td>0.8964</td>\n",
              "      <td>59200.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16944</th>\n",
              "      <td>-124.14</td>\n",
              "      <td>40.67</td>\n",
              "      <td>23.0</td>\n",
              "      <td>580.0</td>\n",
              "      <td>117.0</td>\n",
              "      <td>320.0</td>\n",
              "      <td>109.0</td>\n",
              "      <td>4.2054</td>\n",
              "      <td>130600.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16951</th>\n",
              "      <td>-124.15</td>\n",
              "      <td>40.81</td>\n",
              "      <td>50.0</td>\n",
              "      <td>340.0</td>\n",
              "      <td>74.0</td>\n",
              "      <td>235.0</td>\n",
              "      <td>83.0</td>\n",
              "      <td>1.7500</td>\n",
              "      <td>67500.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16969</th>\n",
              "      <td>-124.17</td>\n",
              "      <td>40.80</td>\n",
              "      <td>52.0</td>\n",
              "      <td>661.0</td>\n",
              "      <td>316.0</td>\n",
              "      <td>392.0</td>\n",
              "      <td>244.0</td>\n",
              "      <td>0.9570</td>\n",
              "      <td>60000.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16982</th>\n",
              "      <td>-124.18</td>\n",
              "      <td>40.62</td>\n",
              "      <td>35.0</td>\n",
              "      <td>952.0</td>\n",
              "      <td>178.0</td>\n",
              "      <td>480.0</td>\n",
              "      <td>179.0</td>\n",
              "      <td>3.0536</td>\n",
              "      <td>107000.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16994</th>\n",
              "      <td>-124.25</td>\n",
              "      <td>40.28</td>\n",
              "      <td>32.0</td>\n",
              "      <td>1430.0</td>\n",
              "      <td>419.0</td>\n",
              "      <td>434.0</td>\n",
              "      <td>187.0</td>\n",
              "      <td>1.9417</td>\n",
              "      <td>76100.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1605 rows × 9 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-2a01e78d-57b1-4dd5-9c23-5d992b671f12')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-2a01e78d-57b1-4dd5-9c23-5d992b671f12 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-2a01e78d-57b1-4dd5-9c23-5d992b671f12');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df[(df['population'] <=500) ] ['median_house_value']"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ce9f8c52-1125-47c7-c03a-f722ad16a94e",
        "id": "iNJeIS6eyR40"
      },
      "execution_count": None,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2         85700.0\n",
              "7         48500.0\n",
              "17        25000.0\n",
              "19        27500.0\n",
              "21        59200.0\n",
              "           ...   \n",
              "16944    130600.0\n",
              "16951     67500.0\n",
              "16969     60000.0\n",
              "16982    107000.0\n",
              "16994     76100.0\n",
              "Name: median_house_value, Length: 1605, dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.query('population < = 500') ['median_house_value'].mean()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CflJ84CBw8LG",
        "outputId": "e48219a1-a3ec-463a-fe2d-6264734c9a03"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "206799.95140186916"
            ]
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=df.query('population < = 500') ['median_house_value'].mean()"
      ],
      "metadata": {
        "id": "7Kt3Rdrw18tE"
      },
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(round(a))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LWc6Iyqy0KVs",
        "outputId": "b2ed4581-7dc0-4688-f33e-cd067a365a72"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "206800\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Задача 42: Узнать какая максимальная households в зоне минимального значения population"
      ],
      "metadata": {
        "id": "csH8Ia1x2bvs"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df[df.population == df['population'].min()] "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 81
        },
        "id": "VhXDqLQt3Aiq",
        "outputId": "581fc21b-d28c-4783-e0a4-0cff8b1dcc86"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "      longitude  latitude  housing_median_age  total_rooms  total_bedrooms  \\\n",
              "8232    -118.44     34.04                16.0         18.0             6.0   \n",
              "\n",
              "      population  households  median_income  median_house_value  \n",
              "8232         3.0         4.0          0.536            350000.0  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-5ea8f5c1-ef11-4450-9953-bbd021cc561e\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>longitude</th>\n",
              "      <th>latitude</th>\n",
              "      <th>housing_median_age</th>\n",
              "      <th>total_rooms</th>\n",
              "      <th>total_bedrooms</th>\n",
              "      <th>population</th>\n",
              "      <th>households</th>\n",
              "      <th>median_income</th>\n",
              "      <th>median_house_value</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>8232</th>\n",
              "      <td>-118.44</td>\n",
              "      <td>34.04</td>\n",
              "      <td>16.0</td>\n",
              "      <td>18.0</td>\n",
              "      <td>6.0</td>\n",
              "      <td>3.0</td>\n",
              "      <td>4.0</td>\n",
              "      <td>0.536</td>\n",
              "      <td>350000.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-5ea8f5c1-ef11-4450-9953-bbd021cc561e')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-5ea8f5c1-ef11-4450-9953-bbd021cc561e button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-5ea8f5c1-ef11-4450-9953-bbd021cc561e');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df[df.population == df['population'].min()] ['households'].max()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xKknsQHN3UsX",
        "outputId": "4bb9e2ac-3180-48a2-a5c3-b87392ec0f8b"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4.0"
            ]
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    }
  ]
}