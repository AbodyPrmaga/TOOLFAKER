from faker import Faker #مكتبة عمل معلومات فيك
from rich.prompt import Prompt # مكتبة تلوين النصوص في الكنسول
from rich.console import Console # مكتبة تلوين النصوص في الكنسول
import pyfiglet # مكتبة تحويل الكلمة الى كلمة كبيرة مخططة بالكنسول
import os #مكتبة التعامل مع النظام
os.system("cls") # امر لحذف اي بيانات في الكنسول اولا قبل البدأ
faker = Faker() # تنشيط مكتبة التوليد 
console = Console() # تنشيط مكتبة التلوين
try:# يشغل البرنامج طول مافي غلط
    wel = pyfiglet.figlet_format(text="Welcome  In V7Tool",width=120,justify="center")#تحويل الكلمة دي لكلمة كبيرة الحجم مخططة
    console.print(f"[bold red]{wel}[/bold red]")#تلوين الكلمةالي فوق ووضعها بالكنسول
    range_ = int(Prompt.ask(("[bold white]Enter Range of Users : [/bold white]")))#هنا يكتب المستخدم عدد اليوزرس

    for i in range(range_):#حلقة تكرار طباعة اليوزرس الي عددهم مكتوب سابقا من قبل المستخدم
        console.print(f"[bold white]User : {faker.name()}[/bold white] || [bold green]Email : {faker.email()} [/bold green]|| [bold red]NumberPhone : {faker.phone_number()}[/bold red]")#طباعة الايميل والرقم الهاتف واسم الشخص مع تلوين جميل

    console.print(f"[bold blue]Done Get About {range_} Users ✔[/bold blue]")#رسالة تعلن انه تم طباعة المستخدمين المطلوبين
    console.print("[bold yellow]Dev By Abdelrahman *__*[/bold yellow]")#نص يثبت انه تم التطوير من قبلي انا
except Exception as ex :#لو في غلط ينفذ دا
    print(f"Error : {ex} !!")#يطبع رسالة الغلط
input("Enter AnyKey For Exit... ")#يطلب من المستخدم ان يضغط علىي مفتاح حتى ينغلق التطبيق