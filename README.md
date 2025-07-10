# Food Organizer: Personalized Weekly Meal Planner

## Overview

Navigating dietary goals can be complex, often requiring meticulous tracking and consistent meal planning. The **Food Organizer** is an intelligent Python application designed to simplify this process by transforming your preferred food choices into a personalized weekly meal plan.

The core idea is simple: **you provide the CSV files detailing the foods you enjoy**, along with their respective nutritional baremos (e.g., "High", "Low", "Moderate"). Based on your selected dietary objective—be it **Volume (Muscle Gain)**, **Definition (Fat Loss)**, or **Maintenance (Weight Management)**—the application processes this data to generate a comprehensive weekly schedule of meals.

A key objective for this tool is to offer significant variety, aiming to avoid meal repetition for at least two weeks. This is made possible by building a large and diverse repository of your favorite foods, allowing the application to intelligently distribute them across your weekly plan. This initial version lays the groundwork for a much more sophisticated and user-friendly meal planning experience.

## Features

* **Customizable Dietary Goal Selection:** Users can effortlessly choose their specific dietary focus from a clear menu, ensuring the generated meals align with their current fitness or health objectives.

* **User-Provided CSV Data Input:** The application's flexibility stems from its ability to read food items and their detailed nutritional profiles directly from CSV files that *you* create and manage. This empowers users to curate their own extensive database of preferred meals.

* **Intelligent Nutritional Categorization:** It processes descriptive nutritional levels (such as "Moderate", "High", "Null" for carbohydrates, proteins, fats, fiber, and added sugars) from your CSVs, converting them into a standardized, usable format. This enables precise filtering based on the specific baremos required for each diet type.

* **Automated Weekly Meal Planning:** Beyond just suggesting a single meal, the system is designed to generate a comprehensive weekly schedule for breakfast, lunch, and dinner, taking into account your chosen dietary goal.

* **Reduced Meal Repetition:** By leveraging a large user-provided food database, the application aims to minimize the repetition of meals within the generated weekly plan, offering diverse options for sustained dietary adherence and enjoyment.

## Getting Started

To run the Food Organizer on your machine, follow these simple steps.

### Prerequisites

* Ensure you have **Python 3.x** installed on your system.

### 1. Clone the Repository

Begin by cloning this project to your local environment:

git clone [https://github.com/your-username/Food-Organizer.git](https://github.com/your-username/Food-Organizer.git)
cd Food-Organizer
(Remember to replace https://github.com/your-username/Food-Organizer.git with the actual URL of your GitHub repository.)

### 2. Prepare Your Custom Data Files

The application's functionality heavily relies on your personalized food database. You will need to create and populate CSV files with your preferred food items and their nutritional baremos. Ensure you have a `data` folder (create one if it doesn't exist) in the project's main directory. Place your CSVs within this `data` folder.

The application specifically looks for these three files:

* `Breakfast-Database.csv`

* `Dinner-Database.csv`

* `Lunch-DataBase.csv`

**CSV File Format:**
Each CSV file must include the following **6 columns** in its header, precisely as named:

`nombre,hidratos de carbono,proteina,grasas,fibra,azucares_añadidos`

The baremo values for nutrients within these columns (e.g., for `hidratos de carbono`, `proteina`, `grasas`, `fibra`, and `azucares_añadidos`) must be one of the following, **in lowercase**:

`"muy bajo", "bajo", "moderado", "alto", "muy alto", "nulo"`

**Example CSV Content (partial):**
nombre,hidratos de carbono,proteina,grasas,fibra,azucares_añadidos
Tortilla 2 huevos + 1 tostada integral,moderado,alto,moderado,moderado,muy bajo
Avena con yogur coco + leche,alto,moderado,moderado,alto,alto
Pollo a la plancha + arroz + ensalada,moderado,alto,bajo,moderado,nulo
Garbanzos aliñados y huevo,alto,alto,moderado,muy alto,nulo

**To achieve significant variety (e.g., for two weeks without repetition), it's highly recommended to fill your CSV databases with a very large number of diverse food items.**

### 3. Run the Application

Once your environment is set up and data files are in place, navigate to the main `Food-Organizer` directory in your terminal or command prompt. Then, execute the application using the following command:
python -m src.main

The program will then prompt you to enter the type of diet (e.g., "volumen", "definicion", "mantenimiento") you wish to generate a plan for.

## Future Enhancements

This is just the foundational version of Food Organizer. We have ambitious plans for its growth, which may include:

* **Advanced Planning Algorithms:** Implementing more sophisticated logic to optimize meal distribution, further minimize repetition, and consider nutritional balance across the week.

* **User Interface:** Developing a user-friendly graphical interface (GUI) to make interaction more intuitive and visually appealing.

* **Custom Baremos & Rules:** Allowing users to define their own baremo values or specific dietary rules directly within the application.

* **Meal Tracking & Analysis:** Features for tracking consumed meals and providing detailed nutritional breakdowns.

* **External Data Integration:** Possibility of connecting to external food databases or recipe APIs.

## Contributing

We enthusiastically welcome contributions to make Food Organizer an even more powerful and helpful tool! Whether you have suggestions for new features, ideas for improving existing functionalities, or find any bugs, please feel free to open an issue or submit a pull request. Your collaboration is highly valued and appreciated.

## License

This project is open source and distributed under the [MIT License](https://opensource.org/licenses/MIT).
