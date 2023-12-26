# AHU反方教务系统（StarRail）使用说明

## 概述

AHU反方教务系统（StarRail）是一个基于Python和MySQL和Django框架的教务管理系统。以下是系统的安装和配置说明。

## 安装步骤

### 1. 安装Python依赖包

在终端中执行以下命令，安装系统所需的Python依赖包：

```bash
pip install -r requirements.txt
```

### 2. 创建MySQL数据库

在MySQL中执行以下命令，创建名为 `StarRail_AHU_EduSys` 的数据库：版本推荐8.0

```sql
CREATE DATABASE `StarRail_AHU_EduSys` DEFAULT CHARACTER SET utf8;
```

### 3. 运行数据库迁移

执行以下命令，运行数据库迁移以初始化数据库表结构：

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. 更新数据库配置

打开 `projects/projects/settings.py` 文件，更新其中的数据库配置信息。

### 5. 初始化数据库

打开 `dataset/databaseInit.py` 文件，更新其中的数据库配置和文件路径信息，然后运行此Python脚本：

```bash
python dataset/databaseInit.py
```

### 6. 启动服务器

执行以下命令，启动系统服务器：

```bash
python manage.py runserver
```

### 7. 访问系统

在浏览器中访问 [http://127.0.0.1:8000/projects/login](http://127.0.0.1:8000/projects/login) 进入系统。

以上步骤完成后，您应该成功启动了AHU反方教务系统，可以通过提供的链接登录系统。


---

# AHU Counterpart Education System (StarRail)

## Usage Instructions:

1. **Install Required Packages:**
   Open Python and install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Create MySQL Database:**
   Open MySQL and create a database: recommended version 8.0
   ```sql
   CREATE DATABASE `StarRail_AHU_EduSys` DEFAULT CHARACTER SET utf8;
   ```

3. **Run Database Migrations:**
   Execute the following commands to run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Update Database Configuration:**
   Update the database configuration in `projects/settings.py` file.

5. **Initialize Database:**
   Update the database configuration and file paths in `dataset/databaseInit.py`, then run the script:
   ```bash
   python dataset/databaseInit.py
   ```

6. **Start the Server:**
   Run the following command to start the server:
   ```bash
   python manage.py runserver
   ```

7. **Access the System:**
   Open your browser and visit [http://127.0.0.1:8000/projects/login](http://127.0.0.1:8000/projects/login).

---

# About

## 课程信息

### 软件工程概论实验

- **开发成员:**
  - 王鸿炜
  - 王帅
  - 马晴川
  - 高睿翀

- **实验地点:**
  - 安徽大学磬苑校区笃行南楼A208
  - 杏园2504 B

