from dataclasses import dataclass, field, asdict
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    keyword: str
    source_url: str = ""
    tags: List[str] = field(default_factory=list)
    content: str = ""
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def display(self) -> str:
        parts = [f"[{self.keyword}]"]
        if self.source_url:
            parts.append(f"来源: {self.source_url}")
        if self.tags:
            parts.append(f"标签: {', '.join(self.tags)}")
        if self.content:
            parts.append(f"内容: {self.content}")
        parts.append(f"时间: {self.created_at}")
        return " | ".join(parts)


def format_notes_as_table(notes: List[KeywordNote]) -> str:
    if not notes:
        return "(无笔记)"
    header = f"{'关键词':<12} {'来源':<30} {'标签':<20} {'内容':<30} {'创建时间':<20}"
    sep = "-" * len(header)
    lines = [header, sep]
    for note in notes:
        kw = note.keyword[:10]
        url = note.source_url[:28] if note.source_url else "-"
        tags = ", ".join(note.tags)[:18] if note.tags else "-"
        content = note.content[:28] if note.content else "-"
        time_str = note.created_at[:18] if note.created_at else "-"
        lines.append(f"{kw:<12} {url:<30} {tags:<20} {content:<30} {time_str:<20}")
    return "\n".join(lines)


def generate_example_notes() -> List[KeywordNote]:
    return [
        KeywordNote(
            keyword="乐鱼体育",
            source_url="https://tiyu-le-yu.com.cn",
            tags=["体育", "娱乐"],
            content="乐鱼体育平台信息",
        ),
        KeywordNote(
            keyword="体育资讯",
            source_url="https://tiyu-le-yu.com.cn/news",
            tags=["新闻", "体育"],
            content="最新体育动态汇总",
        ),
        KeywordNote(
            keyword="竞技赛事",
            source_url="https://tiyu-le-yu.com.cn/events",
            tags=["赛事", "竞技"],
            content="各类体育赛事安排",
        ),
    ]


def search_notes(notes: List[KeywordNote], query: str) -> List[KeywordNote]:
    q = query.lower()
    result = []
    for note in notes:
        if q in note.keyword.lower() or q in note.content.lower():
            result.append(note)
    return result


if __name__ == "__main__":
    notes = generate_example_notes()
    print("所有笔记（表格格式）：")
    print(format_notes_as_table(notes))
    print("\n单个笔记显示：")
    for note in notes:
        print(note.display())
    print("\n搜索 '体育' 的结果：")
    found = search_notes(notes, "体育")
    for note in found:
        print(note.display())