import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist= input_data.read_data_sets("MNIST_data/",one_hot=True) # y labels are oh-encoded
n_train= mnist.train.num_examples
n_validation= mnist.validation.num_examples
n_test= mnist.test.num_examples

                                    
                                                    
                            
