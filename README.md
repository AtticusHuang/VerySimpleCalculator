# 简易计算器
这是一个用[Python](python.org)制作的计算器，使用了[PyQt](https://riverbankcomputing.com/software/pyqt)来制作界面。
## 使用方法
### 如何运行
在Releases中下载.zip格式的文件并解压，运行其中的'计算器.exe'即可开始使用。
### 如何更换语言(2.1版本及以上才有此功能)
将从Releases中下载到的.zip文件解压，即可看到其中的'lang'文件夹：

<img width="300" alt="多文件版本中的lang文件夹" src="https://user-images.githubusercontent.com/97792909/158017402-cd059eab-4270-488c-91d9-74c017e8bdd3.png"><img width="200" alt="双文件版本中的lang文件夹" src="https://user-images.githubusercontent.com/97792909/158017454-2c0d1707-df95-47af-a435-797350ab6d35.png">

(多文件版本及双文件版本中的文件)

打开此文件夹，即可看到其中的'lang.json'文件，如果您未对齐进行修改，其中内容是：

    {
        "NowLanguage": "Chinese"
    }
    
通过修改冒号后面字符串中的内容，即可完成更换语言的操作。例如，将其更换为'English'

    {
        "NowLanguage": "English"
    }
    
其中的内容可以是任何东西(ABC也行)，不过需要保证lang文件夹下有其中的内容+'.json'的文件，例如，如果其中的内容是'Chinese'，此文件夹下就要有'Chinese.json'文件；如果其中的内容是'ABC'，此文件夹下就要有'ABC.json'文件。

<img width="133" alt="lang文件夹下的文件" src="https://user-images.githubusercontent.com/97792909/158018004-ac612011-eb9f-4f5b-923d-e90a3c1c1a68.png">

(lang文件夹下的文件)

我们可以随意打开一个除'lang.json'外的文件，这里我以'Chinese.json'为例：

    {
      "Window_title": "计算器",
      "Process": "算式",
      "Results": "结果",
      "Number": "数字",
      "Symbols": "符号",
      "Operations": "操作",
      "Dot": "点",
      "Equal": "等于",
      "Plus": "加",
      "Minus": "减",
      "times": "乘",
      "Divided": "除",
      "Back": "退格",
      "Clear": "清除",
      "Warning": "警告",
      "Can_not_put_two_decimal_points_in_one_number": "一个数中不能同时有两个小数点!",
      "Divisor_cannot_be_zero_If_you_need_to_enter_a_decimal_with_zero_before_the_decimal_point_press_key_.":
          "除数不能为零!\n如果需要输入小数点前为零的小数,请按'.'键",
      "Please_input_the_current_number_completely_first": "请先把当前的数输入完整"
    }
   
我们可以通过修改其中的文字来创造属于自己的语言。例如，我们可以把其中的第二行

    "Window_title": "计算器"
    
改成

    "Window_title": "jisuanqi"
    
我们再启动计算器，就可以发现程序的语言已经被改变了。

<img width="347" alt="修改后的效果" src="https://user-images.githubusercontent.com/97792909/158018472-a92d7855-4bd9-42e7-a517-4cad0c4f49cb.png">

(修改后的效果)

**注意，修改时只能修改冒号后面的中文，如果修改英文就会报错。**

我们也可以在新建一个名叫'ABC.json'的文件，并且把'language.json'中的语言改成'ABC'。'ABC.json'里面的内容可以从'Chinese.json'里复制过来，再把它稍微修改一下，也可以达到修改语言的目的。像我就将其改成这样：

    {
       "Window_title": "jisuanqi",
       "Process": "suanshi",
       "Results": "jieguo",
       "Number": "shuzi",
       "Symbols": "fuhao",
       "Operations": "caozuo",
       "Dot": "dian",
       "Equal": "dengyu",
       "Plus": "jia",
       "Minus": "jian",
       "times": "cheng",
       "Divided": "chu",
       "Back": "tuige",
       "Clear": "qingchu",
       "Warning": "jinggao",
       "Can_not_put_two_decimal_points_in_one_number": "yigeshuzhongbunengyouliaggexiaoshudian!",
       "Divisor_cannot_be_zero_If_you_need_to_enter_a_decimal_with_zero_before_the_decimal_point_press_key_.":
           "chushubunengweiling!\nruguoxuyaoshuruxiaoshudianqianweilingdexiaoshu,qingan'.'jian",
       "Please_input_the_current_number_completely_first": "qingxianbadangqiandeshushuruwanzheng"
    }
   
修改后的效果如下：

<img width="347" alt="修改后的效果" src="https://user-images.githubusercontent.com/97792909/158018924-fccde05d-7649-44aa-ad09-1ccb7a70b596.png">

## Bug反馈
如果您在使用这个~~Bug~~软件的过程中遇到了Bug，请在[Issues](https://github.com/AtticusHuang/VerySimpleCalculator/issues)中反馈，不要从其他的渠道联系我。~~要不然我可能这辈子都不知道这个Bug~~
