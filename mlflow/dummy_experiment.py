"""
Optional extra-credit: logs a dummy experiment to MLflow.

Run:
    pip install mlflow
    python mlflow/dummy_experiment.py
    mlflow ui   # then open http://localhost:5000
"""

import random
import mlflow


def main():
    mlflow.set_experiment("devops-intern-final-demo")

    with mlflow.start_run():
        # Dummy hyperparameters
        learning_rate = 0.01
        epochs = 5
        mlflow.log_param("learning_rate", learning_rate)
        mlflow.log_param("epochs", epochs)

        # Dummy metric over "training"
        accuracy = 0.0
        for epoch in range(epochs):
            accuracy += random.uniform(0.05, 0.15)
            mlflow.log_metric("accuracy", min(accuracy, 1.0), step=epoch)

        mlflow.log_metric("final_accuracy", min(accuracy, 1.0))
        print("Dummy MLflow run logged successfully.")


if __name__ == "__main__":
    main()
