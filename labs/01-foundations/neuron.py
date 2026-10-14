"""Train one neuron to decide whether to take an umbrella."""
import math
import random

LEARNING_RATE = 1.0
EPOCHS = 2000


def label(cloudy, rain):
    # The rule the neuron must discover from examples alone.
    return 1.0 if rain > 0.5 or (cloudy and rain > 0.3) else 0.0


def make_examples(count):
    examples = []
    for _ in range(count):
        cloudy = random.choice([0, 1])
        rain = random.random()
        examples.append((cloudy, rain, label(cloudy, rain)))
    return examples


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def predict(weights, bias, cloudy, rain):
    return sigmoid(weights[0] * cloudy + weights[1] * rain + bias)


def train(examples):
    weights, bias = [0.0, 0.0], 0.0
    for epoch in range(EPOCHS):
        loss, grad_w, grad_b = 0.0, [0.0, 0.0], 0.0
        for cloudy, rain, target in examples:
            out = predict(weights, bias, cloudy, rain)
            error = out - target
            loss += error**2
            # Backpropagation for one neuron: how the loss changes with the sum.
            slope = 2 * error * out * (1 - out)
            grad_w[0] += slope * cloudy
            grad_w[1] += slope * rain
            grad_b += slope
        n = len(examples)
        weights[0] -= LEARNING_RATE * grad_w[0] / n
        weights[1] -= LEARNING_RATE * grad_w[1] / n
        bias -= LEARNING_RATE * grad_b / n
        if epoch % 200 == 0:
            print(f"epoch {epoch:4d}  loss {loss / n:.4f}")
    return weights, bias


def main():
    random.seed(1)
    weights, bias = train(make_examples(200))
    print(f"learned: cloudy {weights[0]:.2f}  rain {weights[1]:.2f}  bias {bias:.2f}")
    print(f"cloudy, 80% rain  ->  {predict(weights, bias, 1, 0.8):.2f}")
    print(f"clear,  10% rain  ->  {predict(weights, bias, 0, 0.1):.2f}")


if __name__ == "__main__":
    main()
