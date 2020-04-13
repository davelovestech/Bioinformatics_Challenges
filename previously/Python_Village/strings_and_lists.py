# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices a through b and c through d
# (with space in between), inclusively. In other words, we should include
# elements s[b] and s[d] in our slice.

# Sample Dataset
# HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
# 22 27 97 102

# Sample Output
# Humpty Dumpty
def slice_and_dice(text_string, a, b, c, d):
    text_string_ab_slice = text_string[a:b+1]
    text_string_cd_slice = text_string[c:d+1]
    left_space_right_slices = text_string_ab_slice + ' ' + text_string_cd_slice
    return left_space_right_slices
# I tested the code w/ this stuff:
# text = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."
# print(slice_and_dice(text, 22, 27, 97, 102))

text = "vQj40bDqlDzbiEMUobkQ01senjgnUhrxilwiuGrOvisxF7KqgJ7TJbzmwXyaHgdtvqRBiLfWUF9CtI7kMBWwGyxYVfk0rwdZSM3kSDT0hpzfiber73j3R5WgtTrfoIuowfuFq6Za7JQtg8bvug6NdRXxGi27YksMEe6g1vfqyyxBoxxOTWEPMbbFHYNmprubaSPNL."
print(slice_and_dice(text, 39, 42, 107, 111))
