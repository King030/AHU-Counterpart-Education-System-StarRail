from django.db import models


class CharField(models.Field):
    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(CharField, self).__init__(max_length=max_length, *args, **kwargs)

    def db_type(self, connection):
        return 'char(%s)' % self.max_length

class Colleges(models.Model):
    id = models.CharField('学院编号', max_length=13, primary_key=True)
    name = models.CharField('学院名称', max_length=20, null=False)
    createTime = models.CharField('记录时间', db_column='create_time', max_length=19, null=False)
    class Meta:
        db_table = 'colleges'

class Majors(models.Model):
    id = models.CharField('专业编号', max_length=13, primary_key=True)
    name = models.CharField('专业名称', max_length=20, null=False)
    createTime = models.CharField('记录时间', db_column='create_time', max_length=19, null=False)
    class Meta:
        db_table = 'majors'

class Projects(models.Model):
    id = models.CharField('课程编号', max_length=13, primary_key=True)
    name = models.CharField('课程名称', max_length=20, null=False)
    createTime = models.CharField('记录时间', db_column='create_time', max_length=19, null=False)
    location = models.CharField('上课地点', max_length=20, null=False, default='宿舍宿舍 必须在宿舍上课！')
    time = models.CharField('上课时间', max_length=20, null=False, default='早八早八！统统给我上早八！！！！')
    class Meta:
        db_table = 'projects'

class Grades(models.Model):
    id = models.CharField('年级编号', max_length=13, primary_key=True)
    name = models.CharField('年级名称', max_length=20, null=False)
    createTime = models.CharField('记录时间', db_column='create_time', max_length=19, null=False)
    class Meta:
        db_table = 'grades'

class Users(models.Model):
    id = models.CharField('用户编号', max_length=13, primary_key=True)
    userName = models.CharField('用户账号', db_column='user_name', max_length=32, null=False)
    passWord = models.CharField('用户密码', db_column='pass_word', max_length=32, null=False)
    name = models.CharField('用户姓名', max_length=20, null=False)
    age = models.IntegerField('用户年龄', null=False)
    gender = models.CharField('用户性别', max_length=4, null=False)
    type = models.IntegerField('用户身份', null=False)
    class Meta:
        db_table = 'users'

class Students(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, db_column="id", max_length=13, primary_key=True)
    major = models.ForeignKey(Majors, on_delete=models.CASCADE, db_column="major_id", max_length=13)
    college = models.ForeignKey(Colleges, on_delete=models.CASCADE, db_column="college_id", max_length=13)
    grade = models.ForeignKey(Grades, on_delete=models.CASCADE, db_column="grade_id", max_length=13)

    class Meta:
        db_table = 'students'

class Teachers(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, db_column="id", max_length=13, primary_key=True)
    record = models.CharField('教师学历', max_length=8, null=False)
    phone = models.CharField('联系电话', max_length=11, null=False)
    address = models.CharField('联系地址', max_length=32, null=False)
    class Meta:
        db_table = 'teachers'

class WorkPalns(models.Model):
    id = models.CharField('记录编号', max_length=13, primary_key=True)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, db_column="teacher_id", max_length=13, null=False)
    grade = models.ForeignKey(Grades, on_delete=models.CASCADE, db_column="grade_id", max_length=13, null=False)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, db_column="project_id", max_length=13, null=False)
    class Meta:
        db_table = 'work_palns'

class SelectLogs(models.Model):
    id = models.CharField('记录编号', max_length=13, primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE, db_column="student_id", max_length=13, null=True)
    workPaln = models.ForeignKey(WorkPalns, on_delete=models.CASCADE, db_column="plan_id", max_length=13, null=False)
    score = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'select_logs'

class TestLocation(models.Model):
    id = models.CharField('记录编号', max_length=13, primary_key=True)
    workPaln = models.ForeignKey(WorkPalns, on_delete=models.CASCADE, db_column="plan_id", max_length=13, null=False)
    location = models.CharField('考试地点', max_length=20, null=False, default='宿舍宿舍 必须在宿舍考试！')
    time = models.CharField('考试时间', max_length=20, null=False, default='早八早八！统统给我早八考试！！！！')
    class Meta:
        db_table = 'testlocation'