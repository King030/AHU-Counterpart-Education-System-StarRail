function handle(){

    $("button[event=project]").on("click", (e)=>{

        $.ajax({
            url: "/projects/projects/grade",
            type: "GET",
            async: false,
            data:{
                gradeId: $(e.target).attr("data"),
            },
            success: function(res){
                if(res.code == 0){

                    if(res.data && res.data.length > 0){

                       $("#projectList").children().remove();

                       let el = `
                                <label>课程选择</label>
                                <select name="projectId">
                                    <option value="">选择安排的课程</option>
                                `;
                       res.data.forEach(item =>{

                            el = el + `
                                       <option value="${item.id}">${item.name}</option>
                                      `;
                       });
                        el = el + `
                                   </select>
                                  `;
                       $("#projectList").append(el);

                       $.initForm("projectForm", {gradeId: $(e.target).attr("data")});
                       $.model(".projectWin");
                    }else{

                        $.msg("warning", "无可选择的课程");
                    }
                }else{
                    $.msg("error", res.msg);
                }
            }
        });
    });

	$("button[event=upd]").on("click", (e)=>{

        $.ajax({
            url: "/projects/grades/info",
            type: "GET",
            async: false,
            data:{
                id: $(e.target).attr("data"),
            },
            success: function(res){
                if(res.code == 0){

                    $.initForm("updForm", res.data);
                    $.model(".updWin");
                }else{
                    $.msg("error", res.msg);
                }
            }
        });
    });

    $("button[event=del]").on("click", (e)=>{

        $.confirm("确认要删除吗", () =>{

            $.ajax({
                url: "/projects/grades/del",
                type: "POST",
                async: false,
                data:{
                    id: $(e.target).attr("data"),
                },
                success: function(res){
                    if(res.code == 0){
                        $.alert(res.msg, () =>{

                            window.location.reload();
                        });
                    }else{
                        $.msg("error", res.msg);
                    }
                }
            });
        });
    });
}

$(function (){

    let tableView =  {
        el: "#tableShow",
        url: "/projects/grades/page",
        method: "GET",
        where: {
            pageIndex: 1,
            pageSize: 10
        },
        page: true,
        cols: [
            {
                type: "number",
                title: "序号",
            },
            {
				field: "name",
				title: "班级名称",
				align: "center",
			},
			{
				field: "createTime",
				title: "记录时间",
				align: "center",
			},
            {
                 title: "上课安排",
                  template: (d)=>{

                     return `
                             <button type="button" event="project" data="${d.id}" class="fater-btn fater-btn-primary fater-btn-sm">
                                 授课
                             </button>
                             `;
                 }
             },
			{
                title: "操作",
                 template: (d)=>{

                    return `
                            <button type="button" event="upd" data="${d.id}" class="fater-btn fater-btn-primary fater-btn-sm">
                                <span data="${d.id}" class="fa fa-edit"></span>
                            </button>
                            <button type="button" event="del" data="${d.id}" class="fater-btn fater-btn-danger fater-btn-sm">
                                <span data="${d.id}" class="fa fa-trash"></span>
                            </button>
                            `;
                }
            }
        ]
    }
    $.table(tableView);

    $(".fater-btn-form-qry").on("click", ()=>{

        tableView.where["name"] = $("[name=para1]").val();

        $.table(tableView);
        
        handle();
    });

    $("button[event=add]").on("click", ()=>{

        $.model(".addWin");
    });
    

	handle();

    $("#addFormBtn").on("click", ()=>{

        let formVal = $.getFrom("addForm");

        $.ajax({
            url: "/projects/grades/add",
            type: "POST",
            data: formVal,
            success: function(res){
                if(res.code == 0){
                    $.alert(res.msg, () =>{

                        window.location.reload();
                    });
                }else{
                    $.msg("error", res.msg);
                }
            }
        });
    });

    $("#updFormBtn").on("click", ()=>{

        let formVal = $.getFrom("updForm");

        $.ajax({
            url: "/projects/grades/upd",
            type: "POST",
            data: formVal,
            success: function(res){
                if(res.code == 0){
                    $.alert(res.msg, () =>{

                        window.location.reload();
                    });
                }else{
                    $.msg("error", res.msg);
                }
            }
        });
    });

    $("#projectFormBtn").on("click", ()=>{

        let formVal = $.getFrom("projectForm");

        $.ajax({
            url: "/projects/workPalns/add",
            type: "POST",
            data: formVal,
            success: function(res){
                if(res.code == 0){
                    $.alert(res.msg, () =>{

                        window.location.reload();
                    });
                }else{
                    $.msg("error", res.msg);
                }
            }
        });
    });
});