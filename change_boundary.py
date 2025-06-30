import re

def modify_boundary_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # 替换left patch
    content = re.sub(
        r'(left\s*\{[^}]*?type\s*)patch(\s*;[^}]*?\})',
        r'\1cyclicAMI;\n\t\tneighbourPatch\tright;\n\t\tmatchTolerance\t1e-4;\n\t\ttransform\trotational;\n\t\trotationAxis\t(1 0 0);\n\t\trotationCentre\t(0 0 0)\2',
        content,
        flags=re.DOTALL
    )

    # 替换right patch
    content = re.sub(
        r'(right\s*\{[^}]*?type\s*)patch(\s*;[^}]*?\})',
        r'\1cyclicAMI;\n\t\tneighbourPatch\tleft;\n\t\tmatchTolerance\t1e-4;\n\t\ttransform\trotational;\n\t\trotationAxis\t(1 0 0);\n\t\trotationCentre\t(0 0 0)\2',
        content,
        flags=re.DOTALL
    )

    # 替换external wall为patch
    # content = re.sub(
    #     r'(\s*type\s+wall;\s*inGroups\s+1\(wall\);\s*)',
    #     '\ttype            patch;\n\t\t',
    #     content
    # )

    content = re.sub(
        r'external\s*\{.*?type\s+wall;\s*inGroups\s+1\(wall\);\s*',
        'external\n\t{\n\t\ttype            patch;\n\t\t',
        content,
        flags=re.DOTALL  # 确保跨行匹配
    )

    with open(filepath, 'w') as f:
        f.write(content)
    print(f"文件 {filepath} 修改成功")


# Usage
# 这里改成相对路径也可以
# modify_boundary_file("/home/wennx/openfoam_projects/initial/constant/polyMesh/boundary")
modify_boundary_file("./constant/polyMesh/boundary")

