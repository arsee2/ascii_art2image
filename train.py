
def train(model,optimizer,embedding,batch_size = 128):
    '''
    :param model: pytorch model
    :param optimizer: optimizer
    :param batch_size: batch size
    :return:
    '''

    model_name = type(xmodel).__name__
    embedding_name = type(embedding).__name__
    # save path of model weights
    save_model_weights_path = "weights//"+model_name+"+"+embedding_name+".png"
    # save graphic of plots
    # https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib
    save_losses_plot = "visualisation//loss"+model_name+"+"+embedding_name+".png"
    # test the model on several examples and save the plots
    save_test_plot = "visualisation//test" + model_name + "+" + embedding_name + ".png"
    pass



# main part for experiments

if __name__ == "__main__":
    pass