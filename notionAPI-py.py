from notion.client import NotionClient
client = NotionClient(token_v2="e61afbfba5e215988becaebc5d0f585169c8e2b23aa29cd4dea3f8a2371fc232c369ff987d3c2ba5ae481bf3e4c3aa15bfa5b0dff71b6691fe3768d60a322cb83f2c387ee5c98e325c22c7b517ba")
page = client.get_block("https://www.notion.so/9fb6da76f9e0462c848d24fac32ec253?v=10d3b04340b24ff6af977ae81630a660")
posts = page.collection.get_rows()

#input = input("읽어올 데이터를 입력해 주세요 : ")
input='6일차'
print(page)
for post in posts:
    print(post.title)
    if post.title == input:
        print(post.id)
        child_page = client.get_block(post.id)
        print("child_page:", child_page)
        for text in child_page.children:
            print("text:", text)
            print("type:", text.type)


    print()
