def josephus(n, k):
    """
    این تابع شخص آزاد شده در بازی ژوزفوس را با n دزد و گام k
    برمی گرداند.
    """
    # لیستی از دزدان ایجاد می‌کنیم
    people = list(range(1, n + 1))
    # شاخص دزد فعلی
    current_index = 0
    # حلقه تا زمانی که یک دزد در حلقه باقی بماند ادامه پیدا می‌کند
    while len(people) > 1:
        # محاسبه شاخص دزدی که حذف می‌شود
        index_to_remove = (current_index + k - 1) % len(people)
        # حذف دزد از لیست
        people.pop(index_to_remove)
        # به روز رسانی شاخص دزد فعلی
        current_index = index_to_remove % len(people)
    # بازگشت شخص آزاد شده
    return people[0]

# تعداد دفعاتی که باید آزمایش انجام شود
num_tests = int(input())

# انجام آزمایشات
for i in range(num_tests):
    # خواندن ورودی
    n = int(input())
    k = int(input())
    # فراخوانی تابع josephus و چاپ خروجی
    print(josephus(n, k))
