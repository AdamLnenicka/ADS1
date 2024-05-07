
---

# Project - MySQL Docker Instance

## Description
This project aims to set up a MySQL database instance in Docker that meets specific requirements.

In addition to the specified requirements, considerable effort was invested in creating additional Python scripts to automate various database setup tasks. These scripts streamline the process of configuring user roles, creating tables, setting up views, and adjusting database parameters. By voluntarily creating these scripts, the project aims to enhance efficiency and facilitate the setup process for future deployments.

```
proj1
│   docker-compose.yml
│   run_all_tasks.py
│   ADS_2024_projekt_c._1.pdf
│
├── data
│       student_activity.csv
│
├── scripts
│       create_activity_table.py
│       create_database.py
│       create_user.py
│       create_view.py
│       ensure_ordering.py
│       grant_permissions.py
│       set_buffer_pool_size.py
│       set_max_connections.py
│       set_role.py
│       set_timezone.py
│
└── readme.md
```

## Tasks
1. Use the pre-prepared image `niwics/mendeluads24p1` from Docker Hub containing a MySQL server (MariaDB) with a user "root" and password "aaa".
2. Create a user with your login and password "aaa" to allow connection from a remote testing machine.
3. Create a role "student".
4. Assign the "student" role to your user so that it is active immediately upon login.
5. Create a database "mendelu" with a table "activity" containing the same data as the table "mendelu.student_activity".
6. Create a VIEW on the "activity" table named "my_activity" containing only your records and records from the floor with the most entries.
7. Allow the "student" role to read all columns of the "activity" table and the "my_activity" view.
8. Ensure sorting by the "activity" column in the "my_activity" view according to the Czech alphabet.
9. Set the correct time zone for Brno.
10. Reduce the size of the buffer pool to 64 MB.
11. Decrease the maximum number of connections to the minimum value.
12. Run the MySQL Docker instance on external port 8080, accessible from another testing machine.

---
for pulling my image 
```xlnenick/mendeluads:v1```
