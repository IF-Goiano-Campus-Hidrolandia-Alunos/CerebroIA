---
tags: [importado, italo]
updated: 2026-06-21
---

- Cria de forma fácil e rápida um conjunto de serviços SOAP
- O desenvolvedor so precisa escrever o método, que sera convertido para um Serviço
- Cria-se contratos dos serviços automaticamente

```c#
namespace NetFw.Servico
{
	/// <summary>
	/// Descrição resumida de WebService
	/// </summary>
	
	[WebService(Namespace = "http://tempuri.org/")]
	[WebServiceBinding(ConformsTo = WsiProfiles-BasicProfile1_1)]
	[System. ComponentModel. ToolboxItem(false)]
	// Para permitir que esse serviço da web seja chamado a partir do script, usando ASP.NET AJAX,
	// [System-Web.Script.Services.ScriptService]
	public class WebService : System.Web.Services-WebService
	{
		[WebMethod]	
		public string HelloWorld()
		{
			return "Olá, Mundo";
		}
	}
}
```

