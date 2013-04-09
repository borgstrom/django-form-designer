tinyMCEPopup.requireLangPack();

var FormDesignerDialog = {
    init: function(ed) {
        //tinyMCEPopup.resizeToInnerSize();
    },
    insert: function() {
        var ed = tinyMCEPopup.editor,
            dom = ed.dom,
            f = document.forms[0];

        tinyMCEPopup.execCommand('mceInsertContent', false, dom.createHTML('form', {
            'id': f.forms.value,
            'style': 'display: block; width: 300px; height: 200px; background: red;',
        }));

        tinyMCEPopup.close();
    }
};

tinyMCEPopup.onInit.add(FormDesignerDialog.init, FormDesignerDialog);
