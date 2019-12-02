class TextImageDataset(Dataset):

    def __init__(self, root_dir, name_of_datasets):
        '''
        :param root_dir: root directory of all datasets
        :param name_of_datasets: list of dataset names
        '''
        pass

    def __len__(self):
        pass

    def __getitem__(self, idx):
       pass


def get_train_test_val_dataloader():
    '''
    :return: 80%-train 10%-test 10%-val
    '''
    return train, test, val