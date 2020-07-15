#!/usr/bin/python

import datetime as dt

import tensorflow as tf

from 深度学习.tensorflow_demo1 import generate_captcha, captcha_model

b = dt.datetime.now()


if __name__ == '__main__':

    captcha = generate_captcha.generateCaptcha()
    width,height,char_num,characters,classes = captcha.get_parameter()

    x = tf.placeholder(tf.float32, [None, height,width,1])
    y_ = tf.placeholder(tf.float32, [None, char_num*classes])
    keep_prob = tf.placeholder(tf.float32)

    model = captcha_model.captchaModel(width,height,char_num,classes)
    y_conv = model.create_model(x,keep_prob)
    cross_entropy = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=y_,logits=y_conv))
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

    predict = tf.reshape(y_conv, [-1,char_num, classes])
    real = tf.reshape(y_,[-1,char_num, classes])
    correct_prediction = tf.equal(tf.argmax(predict,2), tf.argmax(real,2))
    correct_prediction = tf.cast(correct_prediction, tf.float32)
    accuracy = tf.reduce_mean(correct_prediction)

    saver = tf.train.Saver()
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        step = 0
        while True:
            batch_x,batch_y = next(captcha.gen_captcha(64))
            _,loss = sess.run([train_step,cross_entropy],feed_dict={x: batch_x, y_: batch_y, keep_prob: 0.75})
            e = dt.datetime.now() - b
            print ('step:%d,loss:%f,UseTime:%d s' % (step,loss,e.seconds))     
            if step % 100 == 0:
                batch_x_test,batch_y_test = next(captcha.gen_captcha(100))
                acc = sess.run(accuracy, feed_dict={x: batch_x_test, y_: batch_y_test, keep_prob: 1.})
                print ('###############################################step:%d,accuracy:%f' % (step,acc))
                if acc > 0.99:
                #if True:                
                    #saver.save(sess,"capcha_model.ckpt")
                    #saver.save(sess,'/Anaconda3/mytest',global_step=1,"capcha_model.ckpt")
                    saver.save(sess,'op\\capcha_model.ckpt')
                    #with tf.gfile.FastGFile(op\\mnist.pb, mode = 'wb') as f:
                    #    f.write(output_graph_def.SerializeToString())
                        
                    #tf.gfile.FastGFile('op\\mnist.pb', mode = 'wb').write(output_graph_def.SerializeToString())   
                    tf.train.write_graph(sess.graph_def, 'op\\', 'tfdroid.pbtxt')                       
                    break
            step += 1
			



