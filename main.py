import data_file
# name_1 = input("Hãy nhập tên của bạn: ")
# age_1 = int(input("Bao tuổi?: "))
# name_2 = input("Hãy nhập tên bạn của bạn: ")
# age_2 = int(input("Bao tuổi?: "))
# result = name_1 + " đẹp trai, còn " + name_2 + " xấu trai vãi loz, quỳ xuống con trai ạ"
#
# print(result)
# print(name_1 + " hơn " + name_2 + " " + str(age_1 - age_2) + " tuổi")

user_input_name = input("Nhập tên của bạn: ")
def checktuoi():
    if user_input_name in data_file.team_qc[0:3]:
        # print(str(data_file.team_qc[0:3]) + " hiện đang " + str(data_file.team_age[0]) + " tuổi")
        print("User này có trong team")
    else:
        print("Không tìm thấy tên này trong danh sách!")

checktuoi()