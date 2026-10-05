def convert_to_c_array(tflite_path, output_path, var_name="model_data"):
    with open(tflite_path, 'rb') as f:
        content = f.read()
    with open(output_path, 'w') as f:
        f.write(f'unsigned char {var_name}[] = {{\n')
        for i, byte in enumerate(content):
            f.write(f'0x{byte:02x}, ')
            if (i + 1) % 12 == 0:
                f.write('\n')
        f.write('\n};\n')
        f.write(f'unsigned int {var_name}_len = {len(content)};\n')

convert_to_c_array('drowsy_model_int8.tflite', 'model_data.cc')
print("Done")