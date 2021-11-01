var a = {
    name: 'perspectiva', 
    children: [{
        value: 'soleado', 
        children: [{
            name: 'temperatura', 
            children: [{
                value: 'caliente', 
                children: [{ 'desicion': 'no' }]
            }, 
            {
                value: 'suave', 
                children: [{
                    name: 'humedad', 
                    children: [{
                        value: 'alto', 
                        children: [{ 'desicion': 'no' }]
                    }, 
                    {
                        value: 'normal', 
                        children: [{ 'desicion': 'si' }]
                    }]
                }]
            }, 
            {
                value: 'fresco', 
                children: [{ 'desicion': 'si' }]
            }]
        }]
    }, 
    {
        value: 'nublado', 
        children: [{ 'desicion': 'si' }]
    }, 
    {
        value: 'lluvioso', 
        children: [{
            name: 'viento', 
            children: [{
                value: 'falso', 
                children: [{'desicion': 'si'}]
            }, 
            {
                value: 'cierto', 
                children: [{'desicion': 'no'}]
            }]
        }]
    }]
}