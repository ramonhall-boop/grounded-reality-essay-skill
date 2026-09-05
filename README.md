# Grounded Reality Essay Skill

一个把“从具体生活经验出发 → 拆机制 → 算成本与激励 → 连接制度/历史 → 回到普通人处境”的写作方法，封装成可复用 `SKILL.md` 的 Agent Skill。

> 这是“方法论蒸馏”，不是人物模仿器。它不会要求模型冒充、复刻或逐句模仿任何具体作者的独特文风。

## 适合什么

- 社会观察、教育、就业、阶层流动、商业与生活机制类文章
- 知乎式长回答、公众号观点文、博客文章
- 需要“有故事、有机制、有现实感”，又不想写成空泛鸡汤的内容
- 把一个抽象话题转成普通人能看懂的具体文章

## 核心能力

1. 先找“表面问题背后的真实约束”。
2. 优先用具体人物、物件、数字、时间成本来落地。
3. 用资源、制度、激励、风险、时间、认知差六个镜头拆问题。
4. 用古今/行业/生活类比，把陌生机制讲明白。
5. 强制区分“事实、观察、推断、价值判断”，高风险事实必须核验。
6. 结尾给出一个可复述的“机制句”，而不是口号。

## 目录

```text
skills/grounded-reality-essay/
├── SKILL.md
├── references/
│   ├── distillation.md
│   ├── source-map.md
│   ├── article-architecture.md
│   └── fact-checking.md
├── templates/
│   ├── article-brief.md
│   └── article-output.md
├── examples/
│   └── original-demo.md
└── scripts/
    └── validate_skill.py
```

## 使用方式

这是标准的 `SKILL.md` 结构。支持 Agent Skills 的工具通常可以直接读取这个目录；也可以把 `skills/grounded-reality-essay/` 拷贝到你自己的 skills 目录里。

最简单的调用方式：

```text
使用 grounded-reality-essay，写一篇：为什么很多大学生明知道要实习，却迟迟不投第一份简历？
要求：1500-2000 字，普通大学生视角，不卖惨，不鸡汤，事实不确定就标注。
```

## 数据边界

本版本基于公开可检索到的代表性内容进行方法论提炼，并主动排除了征婚、相亲、恋爱、婚姻、怀孕等相关素材。知乎个人主页存在反爬与登录限制，因此当前语料不是“全量账号导出”。

如果以后拿到更完整的公开文章/回答导出，可以继续向 `references/source-map.md` 增量添加，再迭代这个 skill。

## License

MIT。源文章版权归原作者及原平台，本仓库不收录原文全文，只保存方法论总结、短摘要与公开来源链接。
