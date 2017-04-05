#coding=utf-8
import tensorflow as tf

hello = tf.constant('Hello Tensorflow!')
session = tf.Session()
print session.run(hello)

a = tf.constant(1)
b = tf.constant(2)
print session.run(a + b)
