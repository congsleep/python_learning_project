import data_file
# name_1 = input("Hãy nhập tên của bạn: ")
# age_1 = int(input("Bao tuổi?: "))
# name_2 = input("Hãy nhập tên bạn của bạn: ")
# age_2 = int(input("Bao tuổi?: "))
# result = name_1 + " đẹp trai, còn " + name_2 + " xấu trai vãi loz, quỳ xuống con trai ạ"
#
# print(result)
# print(name_1 + " hơn " + name_2 + " " + str(age_1 - age_2) + " tuổi")

#---------------------------------------------------
# user_input_name = input("Nhập tên của bạn: ")
# def checktuoi():
#     if user_input_name in data_file.team_qc[0:3]:
#         # print(str(data_file.team_qc[0:3]) + " hiện đang " + str(data_file.team_age[0]) + " tuổi")
#         print("User này có trong team")
#     else:
#         print("Không tìm thấy tên này trong danh sách!")
#
# checktuoi()

#---------------------------------------------------
# def cube(num):
#     # result = num*num*num
#     # print(result)
#     return num*num*num
#
# print(cube(5))

#---------------------------------------------------
# def max_num(num_1, num_2, num_3):
#     if num_1 >= num_2 and num_1 >= num_3:
#         print(str(num_1) + " là số lớn nhất")
#     elif num_2 >= num_1 and num_2 >= num_3:
#         print(str(num_2) + " là số lớn nhất")
#     else:
#         print(str(num_3) + " là số lớn nhất")
#
# num1 = input("Nhập số thứ 1: ")
# num2 = input("Nhập số thứ 2: ")
# num3 = input("Nhập số thứ 3: ")
#
# max_num(num1, num2, num3)

#---------------------------------------------------
# monthConversion = {
#     1: "Tháng Một",
#     2: "Tháng Hai",
#     3: "Tháng Ba",
#     4: "Tháng Bốn",
#     5: "Tháng Năm",
#     6: "Tháng sáu",
#     7: "Tháng Bảy",
#     8: "Tháng Tám",
#     9: "Tháng Chín",
#     10: "Tháng Mười",
#     11: "Tháng Mười một",
#     12: "Tháng Mười hai"
# }
#
# print(monthConversion[2])
# print(monthConversion.get(11))

#---------------------------------------------------
# cun = 1
# while cun <= 18:
#     print("Cún đang " + str(cun) + " tuổi.")
#     cun += 1
#     print("Cún đã đủ tuổi")

#---------------------------------------------------

def doan_chu():
    team_qc = ["Công", "Hoa", "Huyền", "Uyên"]
    team_pd = ["Trí", "Trang"]
    team_dev = ["Toàn", "Cường", "Linh"]
    guess_qc = ""
    guess_pd = ""
    guess_dev = ""
    guess_count = 0
    guess_limit = 3
    out_of_guess = False

    while guess_qc not in team_qc or guess_pd not in team_pd or guess_dev not in team_dev:
        if guess_count < guess_limit:
            guess_qc = input("Lần " + str(guess_count + 1) + ". Hãy đoán tên 1 người trong team QC: ")
            guess_pd = input("Lần " + str(guess_count + 1) + ". Hãy đoán tên 1 người trong team PD: ")
            guess_dev = input("Lần " + str(guess_count + 1) + ". Hãy đoán tên 1 người trong team DEV: ")
            guess_count += 1
        else:
            out_of_guess = True
            print("Hết lượt rồi, thử lại sau nhé!")
            return
    if guess_count == 1 and guess_qc in team_qc and guess_pd in team_pd and guess_dev in team_dev:
        print("Kinh thật, mới lần " + str(guess_count) + " đã đoán được rồi. Giỏi quá!")
    else:
        print("Chính xác! Mất " + str(guess_count) + " lần mới đoán được.")

doan_chu()