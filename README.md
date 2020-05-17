# Router

Flask应用路由器，应用托管管理。

## 设计

- 依托于Apache运行。
- 检索目录下的各种app，import对应app，并且挂在对应/{{应用名字}}。
- 尝试用{{name}}.app.lanceliang2001.top访问。
- 拥有前端管理页面。
- 能够动态提交运行应用。

## APP管理

*APP配置*
- router.json：储存app信息。
    - 名字
    - ~~挂载点~~（用名字）
    - import的文件
    - import的app
    - 描述
        - 所有者
        - ~~权限~~
        - 注释