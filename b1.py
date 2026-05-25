student_name = "  nguYEn vAn a  "
student_code = "  rk-001-python  "
email = "  student01@gmail.com  "

student_name = student_name.strip().title()
student_code = student_code.strip().upper()
email = email.strip().lower()

print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)

#C1 Vì strip() trả về chuỗi mới nên không thay đổi trực tiếp student_name.

#C2 Vì title() cũng trả về chuỗi mới, nếu không gán lại thì kết quả không đổi.

#C3 Vì upper() không chỉnh sửa trực tiếp chuỗi gốc mà chỉ tạo chuỗi mới viết hoa.

#C4 Vì lower() chỉ trả về chuỗi mới viết thường chứ không tự cập nhật biến email.

#C5 Muốn các phương thức có hiệu lực cần gán lại giá trị cho biến.
