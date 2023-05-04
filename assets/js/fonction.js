
function supprimerAchat(id){
	swal({
			title: "Etes- vous Sur?",
			text: "Si vous le supprimer , on ne peut pas le recuperer?",
			icon: "warning",
			buttons: true,
			dangerMode: true,
		}).then((willDelete) => {
			if (willDelete) {
				$.ajax({
					type:'GET',
					url:'ajax/form',
					data:({ value:id }),
					success:function($data,$textStatus,$XMLHtpRequest){
						swal({
							title: "",
							text: $data,
							icon: "success",
						}).then((willDelete) => {
							if (willDelete){
								document.location.reload();
							};
						});			
					},
					error:function(){
						swal({
								title: "",
								text: "Il y a erreur au serveur pour le moment!!",
								icon: "error",
						}).then((willDelete) => {
							if (willDelete){
								document.location.reload();
							};
						});
					}
				});
			};
		});
}
function modifierAchat(id,numMat,qte){
	$("#id").val(id);
	$("#numMat").val(numMat);
	$("#qte").val(qte);
}
function modifierMateriel(id, numMat, design, pu, stock) {
	$("#idEdit").val(id);
	$("#numMatEdit").val(numMat);
	$("#designEdit").val(design);
	$("#puEdit").val(pu);
	$("#stockEdit").val(stock);
	$("#modalModif").modal("show")
}
function supprimerMateriel(id){
	swal({
			title: "Etes- vous Sur?",
			text: "Si vous le supprimer , on ne peut pas le recuperer?",
			icon: "warning",
			buttons: true,
			dangerMode: true,
		}).then((willDelete) => {
			if (willDelete) {
				$.ajax({
					type:'GET',
					url:'format',
					data:({ value:id }),
					success:function($data,$textStatus,$XMLHtpRequest){
						swal({
							title: "",
							text: $textStatus,
							icon: "success",
						}).then((willDelete) => {
							if (willDelete){
								document.location.reload();
							};
						});			
					},
					error:function(){
						swal({
								title: "",
								text: "Il y a erreur au serveur pour le moment!!",
								icon: "error",
						}).then((willDelete) => {
							if (willDelete){
								document.location.reload();
							};
						});
					}
				});
			};
		});
}