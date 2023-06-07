OrgChart.templates.group.link = '<path stroke-linejoin="round" stroke="#FFCA28" stroke-width="2px" fill="none" d="M{xa},{ya} {xb},{yb} {xc},{yc} L{xd},{yd}" />';
OrgChart.templates.group.nodeMenuButton = 'active';
OrgChart.templates.group.min = Object.assign({}, OrgChart.templates.group);
OrgChart.templates.group.min.imgs = "{val}";
OrgChart.templates.group.min.img_0 = "";
OrgChart.templates.group.min.description = '<text data-width="250" data-text-overflow="multiline" style="font-size: 14px;" fill="#aeaeae" x="125" y="100" text-anchor="middle">{val}</text>';


var chart = new OrgChart(document.getElementById("tree"), {
    layout: OrgChart.treeRightOffset,
    mouseScrool: OrgChart.none,
    template: "olivia",
    enableDragDrop: true,
    nodeMouseClick: OrgChart.action.edit,
    nodeMenu: {
        details: { text: "Details" },
        edit: { text: "Edit" },
        add: { text: "Add" },
        remove: { text: "Remove" }
    },
    dragDropMenu: {
        addInGroup: { text: "Add in group" },
        addAsChild: { text: "Add as child" }
    },
    nodeBinding: {
        imgs: "img",
        description: "description",
        field_0: "name",
        field_1: "title",
        img_0: "img",

    },
    tags: {
        "group": {
            template: "group",
        },
        "IT-group": {
            subTreeConfig: {
                columns: 2
            }
        },
        "sales-group": {
            subTreeConfig: {
                columns: 1
            }
        },
        "hrs-group": {
            min: true,
            subTreeConfig: {
                columns: 2
            }
        },
        "Ecommerce-group": {
            min: true,
            subTreeConfig: {
                columns: 2
            }
        },
    }
});

var groupContextMenu = new OrgChart.menuUI();
groupContextMenu.init(chart);

chart.on('redraw', function (sender) {
    for (var id in sender.nodes) {
        var node = sender.nodes[id];
        if (node.stChildrenIds.length) {
            var nodeElement = document.querySelector('[data-n-id=' + node.id + ']');
            if (nodeElement) {
                nodeElement.addEventListener('contextmenu', function (e) {
                    e.preventDefault();
                    var id = this.getAttribute('data-n-id');
                    groupContextMenu.show(e.pageX, e.pageY, id, null, {
                        addInGroup: {
                            text: "Add New In Group",
                            icon: OrgChart.icon.add(16, 16, '#ccc'),
                            onClick: function (id) {
                                chart.addNode({ id: OrgChart.randomId(), stpid: id });
                            }
                        }
                    });
                });
            }
        }
    }

    groupContextMenu.hide();
});

chart.on('drop', function (sender, draggedNodeId, droppedNodeId) {
    var draggedNode = sender.getNode(draggedNodeId);
    var droppedNode = sender.getNode(droppedNodeId);

    if (droppedNode.tags.indexOf("group") != -1 && draggedNode.tags.indexOf("group") == -1) {
        var draggedNodeData = sender.get(draggedNode.id);
        draggedNodeData.pid = null;
        draggedNodeData.stpid = droppedNode.id;
        sender.updateNode(draggedNodeData);
        return false;
    }
});

chart.on('click', function (sender, args) {
    if (args.node.tags.indexOf("group") != -1) {
        if (args.node.min) {
            sender.maximize(args.node.id);
        }
        else {
            sender.minimize(args.node.id);
        }
    }
    return false;
});

chart.on('field', function (sender, args) {
    if (args.node.min) {
        if (args.name == "img") {
            var count = args.node.stChildrenIds.length > 5 ? 5 : args.node.stChildrenIds.length;
            var x = args.node.w / 2 - (count * 32) / 2;
            for (var i = 0; i < count; i++) {
                var data = sender.get(args.node.stChildrenIds[i]);
                args.value += '<image xlink:href="' + data.img + '" x="' + (x + i * 32) + '" y="45" width="32" height="32" ></image>';
            }
        }
    }
});

