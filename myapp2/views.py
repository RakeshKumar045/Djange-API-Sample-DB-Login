# def signup(request):
#
#     if request.method == "POST":
#         userName = request.POST["user_name"]
#         firstName = request.POST["first_name"]
#         lastName = request.POST["last_name"]
#         email = request.POST["email_id"]
#         password = request.POST["password"]
#
#         user = User.objects.create_user(username = userName, first_name = firstName, last_Name = lastName,  email = email, password = password)
#         user.save()
#         print("User has created")
#
#     return render(request,"signup.html")


# def register(request):
#
#     if request.method == "POST":
#         userName = request.POST["user_name"]
#         firstName = request.POST["first_name"]
#         lastName = request.POST["last_name"]
#         email = request.POST["email_id"]
#         password = request.POST["password"]
#
#         user = User.objects.create_user(username = userName, first_name = firstName, last_Name = lastName,  email = email, password = password)
#         user.save()
#         print("User has created")
#
#     return render("/","register.html")
#
