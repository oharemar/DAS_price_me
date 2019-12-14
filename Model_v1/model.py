import pickle


# ### Example of prediction:
# input_array = np.array([0., 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 20, 20, 0, 1, 1, 1, 1, 1, 1, 25, 1, 1, 0])
# print(predict(input_array))
def predict(input_array):
    input_array = input_array.reshape(1, -1)
    model = pickle.load(open("model_price_me.dat", "rb"))
    y_pred = model.predict(input_array)
    return y_pred
