training_dataset = tf.keras.utils.image_dataset_from_directory(
    training_directory,
    seed=123,
    image_size=(image_height, image_width),
    batch_size=batch_size
)
