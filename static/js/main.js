// Table
$(document).ready(function () {
  // inspired by http://jsfiddle.net/arunpjohny/564Lxosz/1/
  $(".table-responsive-stack")
    .find("th")
    .each(function (i) {
      $(".table-responsive-stack td:nth-child(" + (i + 1) + ")").prepend(
        '<span class="table-responsive-stack-thead">' +
          $(this).text() +
          ":</span> "
      );
      $(".table-responsive-stack-thead").hide();
    });

  $(".table-responsive-stack").each(function () {
    var thCount = $(this).find("th").length;
    var rowGrow = 100 / thCount + "%";
    //console.log(rowGrow);
    $(this).find("th, td").css("flex-basis", rowGrow);
  });
  $(document).ready(function () {
    $("#mytable #checkall").click(function () {
      if ($("#mytable #checkall").is(":checked")) {
        $("#mytable input[type=checkbox]").each(function () {
          $(this).prop("checked", true);
        });
      } else {
        $("#mytable input[type=checkbox]").each(function () {
          $(this).prop("checked", false);
        });
      }
    });

    $("[data-toggle=tooltip]").tooltip();
  });

  function flexTable() {
    if ($(window).width() < 768) {
      $(".table-responsive-stack").each(function (i) {
        $(this).find(".table-responsive-stack-thead").show();
        $(this).find("thead").hide();
      });

      // window is less than 768px
    } else {
      $(".table-responsive-stack").each(function (i) {
        $(this).find(".table-responsive-stack-thead").hide();
        $(this).find("thead").show();
      });
    }
    // flextable
  }

  flexTable();

  window.onresize = function (event) {
    flexTable();
  };

  // document ready
});

// Input ID
$(document).ready(function () {
  $(
    ".input-group input[required], .input-group textarea[required], .input-group select[required]"
  ).on("keyup change", function () {
    var $form = $(this).closest("form"),
      $group = $(this).closest(".input-group"),
      $addon = $group.find(".input-group-addon"),
      $icon = $addon.find("span"),
      state = false;

    if (!$group.data("validate")) {
      state = $(this).val() ? true : false;
    }

    if (state) {
      $addon.removeClass("danger");
      $addon.addClass("success");
      $icon.attr("class", "glyphicon glyphicon-ok");
    } else {
      $addon.removeClass("success");
      $addon.addClass("danger");
      $icon.attr("class", "glyphicon glyphicon-remove");
    }

    if ($form.find(".input-group-addon.danger").length == 0) {
      $form.find('[type="submit"]').prop("disabled", false);
    } else {
      $form.find('[type="submit"]').prop("disabled", true);
    }
  });

  $(
    ".input-group input[required], .input-group textarea[required], .input-group select[required]"
  ).trigger("change");
});
