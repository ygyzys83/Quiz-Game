# QUIZ GAME  

Test your knowledge of random topics.

<img src="https://github.com/ygyzys83/Quiz-Game/blob/main/images/quiz.PNG" width="250" />

## Description

Answer 20 randomly generated true/false questions on the topic(s) of your choosing.

## Getting Started

* Download the zip and unpack.
* Open the project in your Python IDE.
* Run `main.py`.

### Executing the program

* Changing the quiz parameters: 
  * To change the quiz, Open `data.py` and update the `parameters = {}` dictionary.
    * In order to get the correct parameter values, go to https://opentdb.com/api_config.php to select the preferred options and generate the API link.
    * For example: https://opentdb.com/api.php?amount=20&category=9&difficulty=hard&type=multiple translates to the following quiz parameters:
      ```sh
      parameters = {
      "amount": 20,
      "type": "multiple",
      "category": 9,
      "difficulty": "hard",
      }
      ```


## Authors

* Godman Tan
  * gtprogramming1@gmail.com
