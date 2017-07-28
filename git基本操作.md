- 自报家门
  git config --global user.name ""
  git config --global user.email ""
  //--global 参数，表示这台机器上的所有git仓库都是用这个配置

- 初始化
  git init

- 把文件添加到仓库
  git add readme.txt（readme.txt是上传的文件名+文件类型）

- 把文件提交到仓库
  git commit -m "xxx" ，"xxx"是提交是的备注信息

- 状态查看
  git  status  或者git  diff
  
- 回退到上一个版本
git reset --hard HEAD^

- 查看提交信息
  git log

- 查看
  cat xxx(xxx是需要查看的文件)

- 查看历史
  git reflog

- 撤销操作
  git checkout

- 删除
  rm  readme.txt（删除的文件）

- 删除并提交
  git rm test.txt
  git commit -m "remove test.txt"

- 远程仓库
  创建SSH Key，输入下面命令后，一路回车。产生id_rsa和id_rsa.pub，这两个文件目录(/c/Users/slyq/.ssh/id_rsa)
  ssh-keygen -t rsa -C "your_email@gmail.com"

- 将本地仓库推送到GitHub仓库
  git remote add origin https://xxxx

- 删除远程库
  git remote rm origin

- 本地库所有内容推送到远程库上
  -u Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令。
  git push -u origin master
  在push时出现fast-forwards 时需要先pull然后在push

- clone 仓库
  git clone https://xxxx

- pull远程仓库中的内容 
  git pull origin master

- 创建分支
  git checkout -b dev 这条命令相当于如下两条命令：
  git branch dev（创建分支）
  git checkout dev（切换到分支，不要和撤销操作git check 混淆）

- 查看当前分支
  git branch
  git branch会列出所有分支，当前分支前面会有一个*号，然后就可以在当前分支上正常提交

- 合并
  git merge（合并制定分支到当前分支）

- 删除分支
  git branch -d dev





