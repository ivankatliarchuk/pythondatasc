import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    # your code goes here
    count = len(node.attrib)
    for n in node:
        count += len(n.attrib)
    return count


if __name__ == '__main__':
    N = int(input().strip())
    xml = ""
    for num in range(N):
        xml += input().strip()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
