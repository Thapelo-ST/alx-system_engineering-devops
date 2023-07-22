<h1>Command line for the win challange</h1>

This challange helps you to understand your linux terminal better and trains, and tests your knowledge on it.

<h3>Screenshots</h3>
My screenshots are formated as so. You will find the question at the top, followed by an answer then the result of an answer

              question
                  |
                  v
        answer to the question or solution
                  |
                  v
          results of solution

<h3>File Naming</h3>
The files are named as they are wanted especialy the first task. The are nammed <i>0-first_9_tasks.png</i>, <i>1-next_9_tasks.png</i> and <i>2-next_9_tasks.png</i>. Then the following tasks are <i>0-first_9_tasks<b>_2</b>.png</i> where <b>_2 or _n</b> is the challenge following, like task 2 and so on.

<h3>How the files were uploaded using SFTP</h3>

1. Open Command Prompt in Administrator mode 

2. Changed the directory to where my screenshots are stored in my local directory , in my case <i>C:\Users\Taps\Pictures\Screenshots></i> 

3. Inserted the SFTP command and password thats provided by ALX, to allow access to my sandbox enviroment.
   
         results will be something like this:

         Connected to ----------------.alx-cod.online. (<i>where -------- will be your sandbox id</i>)

         sftp>
  
5. Changed to the directory to where the screenshots were required to be uploaded at.

         sftp> cd root/alx-system_engineering-devops/command_line_for_the_win/

6. Then I used put *.png so it will upload every .png file from my local directory to the sandbox enviroment directory.

         sftp> put *.png

7. Validated that the screenshots were uploaded by using ls

         sftp> ls

8. Then exited the SFTP enviroment and went to my ALX Web Terminal to validate if the files are uploaded

9. Then pushed the files after validation in the ALX Web Terminal


