$("#knowledgebuilder").click(function(e)
{
    e.preventDefault();
    $.ajax(
    {
        type:'GET',
        url:'http://127.0.0.1:5000/legacyknowledgebuilder',

        success: function(response)
        {
            alert(response);
        },
        error: function(XMLHttpRequest, textStatus, errorThrown)
        {
            alert('Please try again');
        }
    })
});


$("#AbendAnalysis").click(function(e)
{
    e.preventDefault();
    $.ajax(
    {
        type:'GET',
        url:'http://127.0.0.1:5000/AbendAnalysis',

        success: function(response)
        {
            alert(response);
        },
        error: function(XMLHttpRequest, textStatus, errorThrown)
        {
            alert('Please try again');
        }
    })
});

$("#Graphs").click(function()
{
    window.location.href='/Graph_analysis';
});
