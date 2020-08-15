import json
filePath='../DeepMimic/data/motions/humanoid3d_spinkick.txt'
with open(filePath) as data_file:
    arguments = json.load(data_file)
print(arguments)
print(arguments.Frames)